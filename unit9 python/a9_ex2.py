import re

def extract_emails(text: str) -> list[str]:
    pattern = r"(?<=\s)(([\w.\-%+]+)@([^_][\w.\-]+)\.([a-zA-Z]{2,}))"
    return [m.group() for m in re.finditer(pattern, text)]


