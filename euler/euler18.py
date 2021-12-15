# 삼각형 모양의 숫자 배열을 따라 가장 큰 합을 찾는 문제
# https://mingrammer.com/project-euler-maximum-path-sum/
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle_leaves = []

for line in triangle.strip().splitlines():
    triangle_leaves.append([int(i) for i in line.split()])

n = len(triangle_leaves)

for i, leaves in enumerate(triangle_leaves[-2::-1]):
    for j, leaf in enumerate(leaves):
        left = triangle_leaves[n-i-1][j]
        right = triangle_leaves[n-i-1][j+1]
        triangle_leaves[n-i-2][j] += max(left, right)

print(triangle_leaves[0][0])

# ref
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