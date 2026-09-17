"""Copia completa del resultado propio, sin seleccionar o reescribir archivos.

Ejecutar SOLO después del check del paper y con el agente detenido.
Uso: python analysis/copiar_lean.py RUTA_PAPERS_IT25KnowledgeEconomy
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys

root=Path(__file__).resolve().parents[1]
source=Path(sys.argv[1]).resolve()
target=root/"lean"
assert source.name=="IT25KnowledgeEconomy" and source.is_dir()
assert (source/"status.json").is_file(),"Falta status generado: revisar la corrida."
assert not target.exists(),"lean/ ya existe; no sobrescribir una corrida inadvertidamente."

def manifest(folder):
    entries={}
    for p in sorted(folder.rglob("*")):
        rel=p.relative_to(folder).as_posix()
        if p.is_symlink():
            entries[rel]={"type":"symlink","target":str(p.readlink())}
        elif p.is_dir():
            entries[rel]={"type":"directory"}
        else:
            entries[rel]={"type":"file","sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
    return entries

before=manifest(source)
shutil.copytree(source,target,symlinks=True)
after=manifest(target)
assert before==after,"La copia no coincide byte a byte con la carpeta generada."
assert before==manifest(source),"La fuente cambió durante la copia; el agente sigue escribiendo."
digest=hashlib.sha256(json.dumps(before,sort_keys=True,ensure_ascii=True).encode()).hexdigest()
summary={"source_folder":"papers/IT25KnowledgeEconomy", "destination":"lean/",
         "copy_method":"shutil.copytree, sin filtros, symlinks=True",
         "files":sum(v["type"]=="file" for v in before.values()),
         "directories":sum(v["type"]=="directory" for v in before.values()),
         "byte_for_byte_equal":True,"manifest_sha256":digest,
         "git_policy":"git add lean/ ordinario; respetar .gitignore generado; nunca git add -f"}
(root/"logs").mkdir(exist_ok=True)
(root/"logs"/"lean-copy.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2))
