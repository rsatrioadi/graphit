import sys
import re

lines = sys.stdin.read()
words = re.findall("[\w'\-\_]+", lines)

pairs = {}
for i in range(1,len(words)):
    key = (words[i-1].lower().replace("_"," "), words[i].lower().replace("_"," "))
    if key in pairs:
        pairs[key] += 1
    else:
        pairs[key] = 1

hi = max(pairs.values())
lo = min(pairs.values())

print("digraph G {")

for (i,j),v in pairs.items():
    w = ((int(v)-(lo-1))/hi)*4
    print("    \""+i+"\"->\""+j+"\"[weight="+str(int(w)+1)+";penwidth="+str(w)+"]")

print("}")

