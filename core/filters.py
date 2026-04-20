def is_excluded(text, exclude_list):
    text = text.lower()
    return any(e in text for e in exclude_list)


def domain_penalty(text):
    text = text.lower()
    penalty = 0

    non_tech = [
        "retail", "store", "sales",
        "marketing", "hr", "finance",
        "health", "nurse", "logistics",
        "operations"
    ]

    for w in non_tech:
        if w in text:
            penalty -= 2

    return penalty
