def ai_recruiter(text, score):
    text = text.lower()

    # -----------------------
    # HARD NO (ruido claro)
    # -----------------------
    noise_keywords = [
        "marketing", "customer success", "pr social",
        "accounting", "hr", "compliance",
        "content writer", "virtual assistant",
        "tiktok", "freelance gtm"
    ]

    for w in noise_keywords:
        if w in text:
            return {
                "decision": "NO APLICAR",
                "reason": "Rol no técnico / fuera de software",
                "bucket": "noise"
            }

    # -----------------------
    # STRONG DEV SIGNAL
    # -----------------------
    strong_dev = [
        "software engineer", "backend", "frontend",
        "fullstack", "devops", "qa engineer",
        "automation", "platform engineer",
        "data engineer", "ai engineer"
    ]

    for w in strong_dev:
        if w in text:
            if score >= 8:
                return {
                    "decision": "APLICAR",
                    "reason": "Perfil técnico fuerte + score alto",
                    "bucket": "top"
                }
            else:
                return {
                    "decision": "TAL VEZ",
                    "reason": "Perfil técnico pero score medio",
                    "bucket": "mid"
                }

    # -----------------------
    # DEFAULT CASE
    # -----------------------
    if score >= 7:
        return {
            "decision": "TAL VEZ",
            "reason": "Score alto pero rol ambiguo",
            "bucket": "mid"
        }

    return {
        "decision": "NO APLICAR",
        "reason": "Bajo score técnico",
        "bucket": "noise"
    }
