import requests

URL = "https://remotive.com/api/remote-jobs"

def fetch():
    res = requests.get(URL)

    if res.status_code != 200:
        return []

    data = res.json().get("jobs", [])

    return [
        {
            "empresa": j.get("company_name", ""),
            "titulo": j.get("title", ""),
            "url": j.get("url", ""),
            "source": "remotive"
        }
        for j in data
    ]
