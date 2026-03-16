import re
from collections import Counter


def extract_topics(text):

    # Basic stopword list to remove meaningless words
    stopwords = {
        "about", "their", "there", "these", "those", "other",
        "using", "which", "where", "while", "within",
        "could", "would", "should", "because", "between"
    }

    # Extract words with length >=5
    words = re.findall(r'\b[a-zA-Z]{5,}\b', text.lower())

    # Remove stopwords
    filtered_words = [w for w in words if w not in stopwords]

    # Count most frequent meaningful words
    common_words = Counter(filtered_words).most_common(5)

    topics = [word for word, count in common_words]

    return topics
