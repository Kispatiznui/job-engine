import csv
import os

CSV_PATH = "jobs.csv"


def load_existing():
    existing = set()

    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)

            for row in reader:
                if len(row) > 1:
                    existing.add(row[1])

    return existing


def save_jobs(jobs):
    file_exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # 👇 HEADER COMPLETO NUEVO
        if not file_exists:
            writer.writerow([
                "empresa",
                "titulo",
                "url",
                "score",
                "decision",
                "bucket",
                "reason",
                "source"
            ])

        for j in jobs:
            writer.writerow([
                j.get("empresa", ""),
                j.get("titulo", ""),
                j.get("url", ""),
                j.get("score", 0),
                j.get("decision", ""),
                j.get("bucket", ""),
                j.get("reason", ""),
                j.get("source", "")
            ])
def save_jobs(jobs):
    file_exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["empresa", "titulo", "url", "score", "source"])

        for j in jobs:
            writer.writerow([
                j["empresa"],
                j["titulo"],
                j["url"],
                j["score"],
                j["source"]
            ])
