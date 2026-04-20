import json

from sources.remoteok import fetch as remoteok
from sources.remotive import fetch as remotive
from sources.adzuna import fetch as adzuna
from sources.arbeitnow import fetch as arbeitnow
from sources.hackernews import fetch as hackernews

from core.scorer import calculate_score
from core.filters import is_excluded, domain_penalty
from core.exporter import load_existing, save_jobs

CONFIG_PATH = "config.json"

# -----------------------
# CONFIG
# -----------------------
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

exclude = [e.lower() for e in config.get("exclude", [])]

# -----------------------
# EXISTING
# -----------------------
existing = load_existing()

# -----------------------
# FETCH ALL SOURCES
# -----------------------
jobs = []
jobs += remoteok()
jobs += remotive()
jobs += adzuna()
jobs += arbeitnow()
jobs += hackernews()

print(f"📦 Total jobs: {len(jobs)}")

# -----------------------
# PROCESS
# -----------------------
final = []

for job in jobs:
    text = f"{job['titulo']} {job['empresa']}"

    if is_excluded(text, exclude):
        continue

    score = calculate_score(text)
    score += domain_penalty(text)

    job["score"] = score

    if job["titulo"] in existing:
        continue

    if score >= 1:
        final.append(job)

# -----------------------
# SORT
# -----------------------
final.sort(key=lambda x: x["score"], reverse=True)

# -----------------------
# SAVE
# -----------------------
save_jobs(final)

# -----------------------
# OUTPUT
# -----------------------
print("\n🔥 TOP JOBS\n")

for j in final[:25]:
    print(f"{j['empresa']} - {j['titulo']} | {j['score']}")
    print(j["url"])
    print(f"[{j['source']}]")
    print()
