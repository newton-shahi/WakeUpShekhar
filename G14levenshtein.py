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
                    prev[j-1] + (ca==cb) #substitution
                )
            )
    
        prev = cur
    return prev[-1]

print(levenshtein_dist("sabin","sabina"))
print(levenshtein_dist("nirmal","nuurmal"))


 

       
