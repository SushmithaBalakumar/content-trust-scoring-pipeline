def calculate_trust_score(source_type, author, published_date):

    score = 0

    # Source reliability
    if source_type == "pubmed":
        score += 0.5
    elif source_type == "blog":
        score += 0.3
    elif source_type == "youtube":
        score += 0.2

    # Author presence
    if author != "Unknown":
        score += 0.2

    # Recency (simplified rule)
    if published_date != "Unknown":
        score += 0.1

    return round(score, 2)