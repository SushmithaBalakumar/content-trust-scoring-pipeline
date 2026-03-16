def calculate_trust_score(source_type, author, content_chunks, published_date="Unknown"):

    # ---------- Source credibility ----------
    SOURCE_WEIGHTS = {
        "blog": 0.25,
        "youtube": 0.20,
        "pubmed": 0.50
    }

    source_weight = SOURCE_WEIGHTS.get(source_type, 0.20)

    # ---------- Author credibility ----------
    author_score = 0.15 if author != "Unknown" else 0

    # ---------- Content depth ----------
    # More content generally indicates richer information
    content_length_score = min(len(content_chunks) / 20, 0.15)

    # ---------- Citation / research indicators ----------
    content_text = " ".join(content_chunks).lower()

    citation_keywords = [
        "study",
        "research",
        "journal",
        "clinical",
        "trial",
        "evidence"
    ]

    citation_score = 0.10 if any(k in content_text for k in citation_keywords) else 0

    # ---------- Recency factor ----------
    # If a publish date exists, give a small boost
    recency_score = 0.05 if published_date != "Unknown" else 0

    # ---------- Final trust score ----------
    trust_score = (
        source_weight
        + author_score
        + content_length_score
        + citation_score
        + recency_score
    )

    return round(min(trust_score, 1.0), 2)
