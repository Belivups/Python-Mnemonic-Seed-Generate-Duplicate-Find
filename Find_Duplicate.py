from collections import Counter
with open('Wallet GenX.txt') as f:
        c=Counter(c.strip() for c in f if c.strip()) 
        for line in c:
                if c[line]>1:
                        print(line)