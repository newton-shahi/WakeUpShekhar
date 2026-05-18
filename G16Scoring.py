
import re
def levenshtein_dist(a:str,b:str)-> int:
    if(a==b):
        return 0
    if(not a):
        return len(b)
    if(not b):
        return len(a)
    prev = list(range(len(b)+1))
    for i, ca in enumerate(a,1):
        cur = [i]
        for j, cb in enumerate(b,1):
            cur.append(
                min(
                    prev[j] +1, #deletion
                    cur[j-1] + 1, #insertion
                    prev[j-1] + (ca!=cb) #substitution
                )
            )
    
        prev = cur
    return prev[-1]

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]','',text)
    text = re.sub(r'\s+',' ',text)
    return text

def fuzzy_score(tokens,words,max_dist:int):
    best = 0.0
    for token in tokens:
        for word in words:
            dist = levenshtein_dist(token,word)
            if dist <= max_dist:
                score = 1 - (dist/max_dist) *0.3
                best = max(best,score)
    
    return best



def fuzzy_check(token:str,words,max_dist:int):
    return any(levenshtein_dist(token,word) <= max_dist  for word in words)

def findFuzzy(text:str):
    clean = normalize(text)
    our_text_tokens = clean.split()
    has_sabin = any(fuzzy_check(small_tokens,sabin_tokens,2) for small_tokens in our_text_tokens)
    print("Score of sabin : ", fuzzy_score(our_text_tokens,sabin_tokens,3))
    has_nirmal = any(fuzzy_check(small_tokens,nirmal_tokens,2) for small_tokens in our_text_tokens)
    if has_sabin:
        print("sabin le bolyo")
    if has_nirmal:
        print("nirmal le bolyo")

sabin_tokens = ["byad","bad"]
nirmal_tokens = ["good","gud"]

findFuzzy("guuud")
findFuzzy("baddd")