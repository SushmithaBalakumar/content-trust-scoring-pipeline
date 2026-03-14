import re
from collections import Counter


def extract_topics(text):

    words = re.findall(r'\b[a-zA-Z]{5,}\b', text.lower())

    common_words = Counter(words).most_common(5)

    topics = [word for word, count in common_words]

    return topics