# Corrida propia de Lean: resultado parcial

## Procedencia y configuración

La tarea de formalización se asignó a **GPT-5.6 Sol (`gpt-5.6-sol`), razonamiento `xhigh`**, mediante un agente de esta sesión. Sus comandos se ejecutaron desde la raíz del clon propio de AppliedModelingLib en `.work/AppliedModelingLib`. No se afirma haber ejecutado un comando CLI de Codex distinto del mecanismo realmente utilizado.

Prompt requerido, incluido literalmente en la instrucción al agente:

```text
Please formalize https://arxiv.org/abs/2312.05481v11 using the
paper-formalization skill and workflow in this repository.
Use IT25KnowledgeEconomy as the paper folder.
```

La solicitud original y las respuestas visibles están en `prompts.md`; los mensajes entre agentes almacenados cifrados se excluyeron. El registro de generación está en `lean/audit/GENERATION_LOG.md`. Revisión inicial de AppliedModelingLib: `2db7d108cd3a2cb10148974bb2a77856e7d87428`. Fuente: PDF arXiv v11, SHA-256 `0b3c727a204f7801a9598dacd7ca7fdb385e21ee6877992ea0eb13c0538d8ebf`. Elan 4.2.4 y Lean 4.30.0-rc2 se instalaron localmente. Los materiales económicos y el Beamer se prepararon por separado; no se atribuye a todo el trabajo el modelo del agente Lean.

## Qué quedó probado

`lake env lean papers/IT25KnowledgeEconomy/MainTheorems.lean` terminó con **código 0**. Contiene cuatro teoremas sin `sorry`:

| Declaración | Alcance comprobado |
|---|---|
| `automatedWorkerWage_of_zeroProfit` | De beneficio cero, renta `r=a`, tamaño de equipo no nulo y ecuación de tiempo, obtiene `w=a(1-h(1-z))` |
| `autonomousBottomWage_gt_baseline_iff` | Para `0<=a<=1/3`, compara las funciones `1/5` y `a/[2(1-a)]`: ganancia estricta si y solo si `a>2/7` |
| `copilotBottomWage_dominates` | Para `1/5<a<=1/3`, el salario bajo definido para copiloto supera el inicial y el autónomo |
| `copilotTopWage_is_lower` | Compara las funciones salariales superiores definidas; su lectura económica se limita al tramo donde describen el equilibrio |

Esto verifica **álgebra sobre premisas y funciones explícitas**. No demuestra en Lean que esas funciones sean salarios de un equilibrio discreto factible y óptimo: esa interpretación se comprueba por derivación, SymPy y programación lineal fuera de Lean. Tampoco construye el equilibrio continuo del artículo.

El build `lake build +IT25KnowledgeEconomy` también terminó con **código 0**, pero emitió dos advertencias por los `sorry` de las Proposiciones 5 y 6. Por tanto, ese build exitoso no certifica las dos proposiciones.

## Qué sigue abierto y por qué

- Las Proposiciones 5 y 6 tienen interfaces provisionales y endpoints con **dos `sorry` explícitos**. No cuentan como teoremas probados.
- El campo `sourceModelAssumptions : Prop` no desarrolla todavía la densidad continua, la asignación medible, las restricciones de tiempo, la optimización de empresas ni el vaciado de mercados. Una proposición abstracta no establece por sí sola relación alguna entre esos objetos y los salarios. Por ello, la interfaz necesita completar su traducción semántica antes de intentar una prueba del resultado original.
- Las Proposiciones 1–4 están inventariadas, pero no formalizadas con sus enunciados y pruebas completos.
- La revisión semántica independiente y el cierre de auditoría de AppliedModelingLib no se presentan como aprobados. La aprobación humana tampoco se inventó.

El primer scaffold con inventario intentó importar la biblioteca completa y disparó una compilación extensa. Se interrumpió y se utilizó la entrada oficial de creación sin ese inventario, completando después los registros del paper. Windows requirió además un adaptador local para `fcntl`; los detalles y comandos quedan en el informe generado. No se reescribió el workflow upstream para ocultar el problema.

## Check obligatorio y copia

Resultado del comando obligatorio: **no completado**. El check construyó `PaperInterface` correctamente y después quedó sin salida adicional durante aproximadamente 90 segundos. Se interrumpió para respetar el límite de créditos indicado por el usuario; el proceso salió con código 1 por la interrupción. **No es un check aprobado ni un fallo matemático identificado por el checker.** Salida literal: [logs/lean-fast-check.txt](logs/lean-fast-check.txt). Build previo: [logs/lean-build.txt](logs/lean-build.txt).

```bash
python3 scripts/paper_contribution.py check IT25KnowledgeEconomy --fast
```

La carpeta completa `papers/IT25KnowledgeEconomy/` se copió a `lean/` mediante `analysis/copiar_lean.py`, sin filtros, renombres internos ni reescrituras. La igualdad byte a byte está registrada en [logs/lean-copy.json](logs/lean-copy.json). El staging usa `git add lean/` ordinario, respetando el `.gitignore` generado. Nunca se utiliza `git add -f`. El PDF fuente y su texto extraído permanecen en la copia local pero se excluyen de Git.

Los archivos auxiliares del scaffold se conservan aparte en `reproducibility/`. El registro propio de generación está en `lean/audit/GENERATION_LOG.md`; el informe original generado está en `lean/FINAL_VALIDATION_REPORT.md`. Se preservan incluso los artefactos parciales y pendientes de auditoría. La documentación derivada que no llegó a generarse no se fabricó durante la copia.
