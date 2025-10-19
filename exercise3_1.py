import re

def moderate_content(text):
    # list of banned and mild words
    banned_words = ["hate", "kill", "racist", "terror", "suicide"]
    mild_words = ["stupid", "idiot", "dumb"]
    
    risk_score = 0
    clean_text = text

    # check for banned (high-risk) words
    for word in banned_words:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            clean_text = re.sub(rf"\b{word}\b", "****", clean_text, flags=re.IGNORECASE)
            risk_score += 3

    # check for mild (medium-risk) words
    for word in mild_words:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            clean_text = re.sub(rf"\b{word}\b", "****", clean_text, flags=re.IGNORECASE)
            risk_score += 1

    # extra safety rule: detect personal information (email or phone number)
    if re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text):
        risk_score += 2
        clean_text = re.sub(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", "[email removed]", clean_text)

    if re.search(r"\b\d{8,}\b", text):
        risk_score += 2
        clean_text = re.sub(r"\b\d{8,}\b", "[number removed]", clean_text)

    # classify risk level
    if risk_score == 0:
        risk_level = "low"
    elif risk_score <= 3:
        risk_level = "medium"
    else:
        risk_level = "high"

    return {"clean_text": clean_text, "risk_score": risk_score, "risk_level": risk_level}
