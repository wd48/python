n=int(input())
tree=[]
for _ in range(n):
    tree.append(list(map(int, input().split())))

dp=[tree[0][0]]
for i in range(1, n):
    a=[]
    for j in range(i+1):
        if j==0:
            a.append(dp[0]+tree[i][0])
            continue
        elif j==i:
            a.append(dp[-1]+tree[i][-1])
            continue
        if dp[j]>=dp[j-1]:
            a.append(dp[j]+tree[i][j])
        else:
            a.append(dp[j-1]+tree[i][j])
    dp=a

print(max(dp))