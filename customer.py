class ap:
    def __init__(self, id, username, subPackage, showStreaming, views):
        self.id = id
        self.username = username
        self.subPackage = subPackage
        self.showStreaming = showStreaming
        self.views = views


def findRemainingDays(apm, newid, days):
    result = 0
    for ap1 in apm:
        if ap1 != 'null':
            if ap1.id == newid:
                result = ap1.subPackage-days
                break
            else:
                return 0
        else:
            print("error")
            break
    return result

def getDetails(apm, show):
    c = []
    k = 0
    for ap2 in apm:
        if ap2 != 'null':
            if ap2.showStreaming == show:
                k = k + 1
                c[k] = ap2.views
        else:
            break
    l = len(c)
    for i in range(0, l):
        for j in range(i+1, l):
            if c[i] > c[j]:
                temp = c[i]
                c[i] = c[j]
                c[j] = temp

    p = []
    x = 0
    for ap3 in apm:
        if ap3 != 'null':
            for i in range(1, l+1):
                if ap3.views == c[i]:
                    x += 1
                    q = apm.id
                    w = apm.username
                    e = apm.views
                    p[x] = apm(q, w, 0, "", e)
    return p

am = []


for i in range(0, 2):
    id = int(input())
    username = input()
    subPackage = int(input())
    showStreaming = input()
    views = int(input())
    am[i] = ap(id, username, subPackage, showStreaming, views)

newid = int(input())
days = int(input())
show = input()

sol = findRemainingDays(am, newid, days)
if sol > 0:
    print(sol)
else:
    print("its time to recharge")


put = getDetails(am, show)
for u in put:
    print(u.id)
    print(u.username)
    print(u.views)

