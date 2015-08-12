
#find rule from string, start with 3 char and expand
import re

f1=open('starbucks.txt','r')

strings=[s.lower() for s in f1]
print len(strings)

rule={}
for len_ in range(3,10):
    for s in strings:
        for i in range(len(s)-len_):
            s2=s[i:i+len_]
            if ' ' not in s2:
                if (len_,s2) not in rule:
                    rule[(len_,s2)]=0
                rule[(len_,s2)]+=1
                    
max_=sorted(list(set([v for v in rule.values()])))
best=[(k,v) for k,v in rule.iteritems() if v in max_[len(max_)-10:]]
print sorted(best)
            

f1.close()
