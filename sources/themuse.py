import requests

BASE_URL = "https://www.themuse.com/api/public/jobs"

def fetch():
    jobs = []

    try:
        params = {
            "page": 1
        }

        res = requests.get(BASE_URL, params=params)

        if res.status_code != 200:
            return []

        data = res.json().get("results", [])

        for j in data:
            jobs.append({
                "empresa": j.get("company", {}).get("name", ""),
                "titulo": j.get("name", ""),
                "url": j.get("refs", {}).get("landing_page", ""),
                "source": "themuse"
            })

    except Exception as e:
        print("Muse error:", e)

    return jobs
