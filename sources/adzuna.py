import requests

APP_ID = "TU_ID"
APP_KEY = "TU_KEY"

def fetch():
    url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": "junior developer remote"
    }

    res = requests.get(url, params=params)

    if res.status_code != 200:
        return []

    data = res.json().get("results", [])

    jobs = []

    for j in data:
        jobs.append({
            "empresa": j.get("company", {}).get("display_name", ""),
            "titulo": j.get("title", ""),
            "url": j.get("redirect_url", ""),
            "source": "adzuna"
        })

    return jobs
