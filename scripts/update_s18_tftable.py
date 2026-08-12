#!/usr/bin/env python3
"""Incrementally merge TFTable Set 18 official terms into locale CSVs and workspace glossary.

Sources currently published by TFTable: en, zh, ko, fr.
Matches entities strictly by stable entity ID. Existing rows are never changed.
"""
import csv, json, os, urllib.request
from pathlib import Path

BASE = "https://tftable.cc"
LOCALES = {"en":"en", "zh":"zh-CN", "ko":"ko", "fr":"fr"}
TYPES = ["entity-units", "entity-traits", "entity-items", "entity-augments", "entity-wisps"]
ROOT = Path(__file__).resolve().parents[1]
GLOSSARY_DIR = ROOT / "glossaries"
WORKSPACE_GLOSSARY = Path("/home/xing/.openclaw/workspace-tft/data/glossary.json")
CACHE = ROOT / "meta" / "tftable-s18"
CACHE.mkdir(parents=True, exist_ok=True)

def fetch_json(url):
    req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def download():
    out={}
    for locale in LOCALES:
        manifest=fetch_json(f"{BASE}/{locale}/__shared/manifest.json")
        s18=manifest["sets"]["set18"]
        out[locale]={}
        for typ in TYPES:
            rel=s18[typ]
            data=fetch_json(f"{BASE}/{locale}/__shared/{rel}")
            out[locale][typ]=data
            (CACHE/f"{locale}-{typ}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2))
    return out

def names_by_id(data):
    maps={}
    for locale, groups in data.items():
        maps[locale]={}
        for typ, entities in groups.items():
            cur={}
            for eid,e in entities.items():
                name=(e.get("name") or "").strip()
                if name: cur[eid]=name
                if typ=="entity-units":
                    ab=e.get("ability") or {}
                    an=(ab.get("name") or "").strip()
                    if an: cur[eid+"::ability"]=an
            maps[locale][typ]=cur
    return maps

def append_csvs(maps):
    counts={}
    for target_locale,lang_code in LOCALES.items():
        if target_locale=="en":
            continue  # repo has no English target CSV
        path=GLOSSARY_DIR/f"tft_{lang_code}.csv"
        existing=set()
        with path.open(newline="") as f:
            for row in csv.reader(f):
                if len(row)>=2: existing.add((row[0],row[1]))
        rows=[]
        for typ in TYPES:
            target_map=maps[target_locale][typ]
            for eid,target in target_map.items():
                for source_locale in LOCALES:
                    source=maps[source_locale][typ].get(eid)
                    if source and source != target and (source,target) not in existing:
                        rows.append([source,target,lang_code])
                        existing.add((source,target))
        if rows:
            with path.open("a",newline="") as f: csv.writer(f).writerows(rows)
        counts[lang_code]=len(rows)
    return counts

def merge_workspace(maps):
    rows=json.loads(WORKSPACE_GLOSSARY.read_text())
    keys={(r.get("type"),r.get("set"),r.get("id"),r.get("en"),r.get("zh")) for r in rows}
    add=[]
    type_map={"entity-units":"champion","entity-traits":"trait","entity-items":"item","entity-augments":"augment","entity-wisps":"wisp"}
    for typ in TYPES:
        en=maps["en"][typ]; zh=maps["zh"][typ]
        for eid,en_name in en.items():
            zh_name=zh.get(eid)
            if not zh_name: continue
            is_ability=eid.endswith("::ability")
            rowtype="ability" if is_ability else type_map[typ]
            key=(rowtype,"TFTSet18",eid,en_name,zh_name)
            if key not in keys:
                add.append({"type":rowtype,"set":"TFTSet18","en":en_name,"zh":zh_name,"id":eid})
                keys.add(key)
    if add:
        rows.extend(add)
        WORKSPACE_GLOSSARY.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n")
    return len(add)

def main():
    data=download(); maps=names_by_id(data)
    counts=append_csvs(maps)
    merged=merge_workspace(maps)
    summary={"csv_appended":counts,"workspace_glossary_added":merged,
             "entity_counts":{l:{t:len(g) for t,g in gs.items()} for l,gs in data.items()}}
    (CACHE/"last-update.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
