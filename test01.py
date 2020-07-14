def bj15649():
    n, m = (int(i) for i in input().split(' '))
    values = []
    def recur(count):
        for i in range(1,n+1):
            if count == m:
                print()
                return
            if i not in values:
                values.append(i)
                recur(count+1)
                values.pop()
    recur(0)

bj15649()