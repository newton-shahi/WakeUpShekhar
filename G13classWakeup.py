#A WakeDetector class with a constructor that accepts language parameter, a detect(text) 
#method, and a stats() method returning detection count since creation. 
#Test with 5 phonetic variations.
import re
class WakeDetector:
    def __init__(self,wakeUp:dict):
        self.wakeUp = wakeUp
        self.detectCount = 0
        
    def stats(self):
        return self.detectCount
    
    def detect(self,text):
        result = self.exactness(text)
        if(not result):
            print("not detected")
            return
        detect,word,charac,sco = result.items()

        if(detect[1] == True):
            print("Detected")
            self.detectCount = self.detectCount +1


    def normalize(self,text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^a-z\s]','',text)
        text = re.sub(r'\s+',' ',text)
        return text

    def exactness(self,text:str) -> dict | None:
        clean = self.normalize(text)
        for character,saying in self.wakeUp.items():
            for say in saying:
                if say in clean:
                    return {"Detected": True, "detected_word":say,"character":character,"score":1.0}
        return None

WAKEUP_PHRASE = {
    "sabin" : ["haha","i am sabin","i am bad boy"],
    "nirmal" : ["hehe","i am nirmal"]
}

wake1 = WakeDetector(WAKEUP_PHRASE)
wake1.detect("I  am   good   boy!!!!")

wake1.detect("hehe i am nirmal!!!!")
print(wake1.stats())