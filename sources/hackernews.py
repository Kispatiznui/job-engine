import requests

URL = "https://hacker-news.firebaseio.com/v0/jobstories.json"

def fetch():
    res = requests.get(URL)

    if res.status_code != 200:
        return []

    ids = res.json()

    jobs = []

    for job_id in ids[:30]:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{job_id}.json"
        ).json()

        jobs.append({
            "empresa": "HackerNews",
            "titulo": item.get("title", ""),
            "url": item.get("url", f"https://news.ycombinator.com/item?id={job_id}"),
            "source": "hackernews"
        })

    return jobs
