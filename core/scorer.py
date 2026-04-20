def calculate_score(text):
    text = text.lower()
    score = 0

    strong = [
        "qa", "tester", "testing", "automation",
        "selenium", "qa engineer", "test engineer"
    ]

    mid = [
        "developer", "engineer", "software",
        "backend", "frontend", "fullstack",
        "python", "docker", "git"
    ]

    entry = [
        "junior", "entry level", "intern",
        "trainee", "remote", "no experience"
    ]

    for w in strong:
        if w in text:
            score += 4

    for w in mid:
        if w in text:
            score += 2

    for w in entry:
        if w in text:
            score += 2

    return score
