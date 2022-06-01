import re

import requests

# retrieve Moby Dick from the Gutenberg Project

_mobydick_text = requests.get(
    "https://www.gutenberg.org/files/2701/2701-0.txt"
).content.decode("utf-8-sig")

# remove all non-alphabetic characters

_mobydick_normalized_text = re.sub(
    r"\s+",
    " ",
    re.sub(
        r"[^a-zA-Z\s]+",
        "",
        _mobydick_text)).lower()

# split into tokens

mobydick_tokens = _mobydick_normalized_text.split()
