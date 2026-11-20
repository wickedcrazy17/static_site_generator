import re

def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
