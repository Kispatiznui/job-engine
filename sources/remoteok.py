import requests
from urllib.parse import urljoin

URL = "https://remoteok.com/api"

def fetch():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(URL, headers=headers)

    if res.status_code != 200:
        return []

    data = res.json()[1:]

    jobs = []

    for j in data:
        jobs.append({
            "empresa": j.get("company", ""),
            "titulo": j.get("position", ""),
            "url": urljoin("https://remoteok.com", j.get("url", "")),
            "source": "remoteok"
        })

    return jobs
