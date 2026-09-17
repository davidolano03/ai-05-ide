"""Exporta mensajes visibles propios, sin análisis interno ni trazas de revisión.

Uso local: python analysis/exportar_prompts.py RUTA_JSONL_DE_ESTA_SESION
El archivo raw de la sesión permanece privado y no se incluye en la entrega.
"""
import json
import sys
from pathlib import Path

root=Path(__file__).resolve().parents[1]
rows=[]
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    try:
        record=json.loads(line)
    except json.JSONDecodeError:
        continue
    if record.get("type")!="response_item":
        continue
    p=record["payload"]
    if p.get("type")=="message":
        role=p.get("role")
        content="\n".join(b.get("text","") for b in p.get("content",[]) if b.get("type") in {"input_text","output_text","text"})
        if role=="user" and content.startswith("Codex, al igual"):
            rows.append(("Usuario: instrucciones originales", content))
        elif role=="assistant" and p.get("channel") in {None,"commentary","final"} and content:
            rows.append(("Asistente: respuesta visible",content))
    elif p.get("type")=="function_call" and p.get("name","").endswith("spawn_agent"):
        try:
            args=json.loads(p["arguments"])
        except (KeyError,json.JSONDecodeError):
            continue
        if args.get("task_name")=="formalizacion_lean":
            rows.append(("Configuración de la corrida Lean (argumento raw)",p["arguments"]))
    elif p.get("type")=="function_call" and p.get("name","").endswith("send_message"):
        try:
            args=json.loads(p["arguments"])
        except (KeyError,json.JSONDecodeError):
            continue
        if args.get("target")=="formalizacion_lean":
            rows.append(("Seguimiento enviado al agente Lean (raw)",args["message"]))
assert any(title.startswith("Usuario") for title,_ in rows),"No se encontró el prompt original: no inventar una transcripción."
text="# Prompts y respuestas relevantes, raw\n\nSelección literal de mensajes visibles de esta sesión propia. Los títulos son metadatos editoriales; el contenido de los bloques no se reescribió. Se omiten razonamiento interno, instrucciones de sistema, credenciales y trazas privadas. No es un diálogo reconstruido.\n\n"
for i,(title,content) in enumerate(rows,1):
    text+=f"## {i}. {title}\n\n````text\n{content}\n````\n\n"
text+="La respuesta final raw de la corrida Sol, cuando esté disponible, se conserva en `logs/lean-agent-final.md`. Los fallos y comprobaciones se documentan en `LEAN_RUN.md` y en los artefactos originales de `lean/`.\n"
(root/"prompts.md").write_text(text,encoding="utf-8")
print(f"Exportados {len(rows)} mensajes relevantes sin reescribirlos.")
