"""
URL of problem :- https://www.hackerrank.com/contests/code-help-5/challenges/karsha-has-a-problem-/problem

"""

n = int(input())

ns = [int(x) for x in input().split(' ') if x != '' and x!='\n']

d = dict()


for i in ns:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
l = len(ns)
acc = sorted(d.values(), reverse=True)
#print(acc)
updated_len = l
ans = 0
for i in acc:
    if updated_len > (l//2) :
        
        a = acc.pop(0)
        updated_len -= a
        ans += 1
        
print(ans)