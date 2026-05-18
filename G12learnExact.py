import re

#built up on previous lesson, this time we check exactness by comparing with the phrases

WAKEUP_PHRASE = {
    "sabin" : ["haha","i am sabin","i am bad boy"],
    "nirmal" : ["hehe","i am nirmal"]
}

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]','',text)
    text = re.sub(r'\s+',' ',text)
    return text

def exactness(text:str) -> dict | None:
    clean = normalize(text)
    print(clean)
    for character,saying in WAKEUP_PHRASE.items():
        for say in saying:
            if say in clean:
                return {"Detected": True, "detected word":say,"character":character,"score":1.0}
    return None

print(exactness("I  am   bad   boy!!!!"))
print(exactness("hehe i am nirmal hehe"))



