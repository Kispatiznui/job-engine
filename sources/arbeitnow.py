import requests

URL = "https://www.arbeitnow.com/api/job-board-api"

def fetch():
    res = requests.get(URL)

    if res.status_code != 200:
        return []

    data = res.json().get("data", [])

    jobs = []

    for j in data:
        jobs.append({
            "empresa": j.get("company_name", ""),
            "titulo": j.get("title", ""),
            "url": j.get("url", ""),
            "source": "arbeitnow"
        })

    return jobs
