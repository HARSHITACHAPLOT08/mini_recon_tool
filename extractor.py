import re

def extract_emails(text):
    pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    return re.findall(pattern, text)

def extract_links(text):
    pattern = r'href=["\'](.*?)["\']'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r"\+?\d[\d -]{8,12}\d"
    return re.findall(pattern, text)