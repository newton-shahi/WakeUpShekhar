import re
#We will first lower and then remove everything except letter. So its easier to analyze.
def normalize(text:str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]','',text)
    text = re.sub(r'[\s+]',' ',text).strip()
    return text

print(normalize("heyyyy!!! deeepaaa!"))


