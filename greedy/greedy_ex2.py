# 숫자 카드 게임 (greedy)

n,m = map(int, input().split())
result = 0

for _ in range(n):
    arr=list(map(int,input().split()))
    min_num=min(arr)
    result=max(min_num,result)

print(result)