import json

from sources.remoteok import fetch as remoteok
from sources.remotive import fetch as remotive
from sources.arbeitnow import fetch as arbeitnow
from sources.hackernews import fetch as hackernews
from sources.adzuna import fetch as adzuna
from sources.themuse import fetch as themuse

from core.scorer import calculate_score
from core.filters import is_excluded, domain_penalty
from core.exporter import load_existing, save_jobs
from core.recruiter_ai import ai_recruiter

# -----------------------
# CONFIG
# -----------------------
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

exclude = [e.lower() for e in config.get("exclude", [])]

# -----------------------
# EXISTING JOBS
# -----------------------
existing = load_existing()

# -----------------------
# FETCH ALL SOURCES
# -----------------------
jobs = []
jobs += remoteok()
jobs += remotive()
jobs += arbeitnow()
jobs += hackernews()
jobs += adzuna()
jobs += themuse()

print(f"📦 Total jobs raw: {len(jobs)}")

# -----------------------
# BUCKETS (NO SE BORRA NADA)
# -----------------------
top = []
mid = []
noise = []

processed_jobs = []

# -----------------------
# PROCESSING
# -----------------------
for job in jobs:
    text = f"{job['titulo']} {job['empresa']}"

    # filtro suave (solo evita basura configurada)
    if is_excluded(text, exclude):
        continue

    # SCORE BASE
    score = calculate_score(text)
    score += domain_penalty(text)

    job["score"] = round(score, 2)

    # DECISIÓN IA RECRUITER
    decision = ai_recruiter(text, score)

    job["decision"] = decision["decision"]
    job["reason"] = decision["reason"]
    job["bucket"] = decision["bucket"]

    # evitar duplicados
    if job["titulo"] in existing:
        continue

    # -----------------------
    # CLASIFICACIÓN
    # -----------------------
    if decision["bucket"] == "top":
        top.append(job)
    elif decision["bucket"] == "mid":
        mid.append(job)
    else:
        noise.append(job)

    processed_jobs.append(job)

# -----------------------
# ORDENAR POR SCORE
# -----------------------
top.sort(key=lambda x: x["score"], reverse=True)
mid.sort(key=lambda x: x["score"], reverse=True)
noise.sort(key=lambda x: x["score"], reverse=True)

# -----------------------
# GUARDAR TODO (INCLUYE RUIDO)
# -----------------------
save_jobs(processed_jobs)

# -----------------------
# OUTPUT
# -----------------------
print("\n🔥 APLICAR (TOP JOBS)\n")
for j in top[:20]:
    print(f"{j['empresa']} - {j['titulo']} | {j['score']}")
    print(f"DECISIÓN: {j['decision']} | {j['reason']}")
    print(j["url"])
    print()

print("\n🟡 TAL VEZ\n")
for j in mid[:20]:
    print(f"{j['empresa']} - {j['titulo']} | {j['score']}")
    print(f"DECISIÓN: {j['decision']} | {j['reason']}")
    print()

print("\n⚪ RUIDO (NO BORRADO, SOLO SEPARADO)\n")
for j in noise[:20]:
    print(f"{j['empresa']} - {j['titulo']}")
    print(f"DECISIÓN: {j['decision']}")
    print()
