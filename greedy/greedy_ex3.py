# 1이 될때까지 (greedy)

n,k = map(int,input().split())

cnt = 0

while n!=1:
    if n % k == 0 :
        n//=k
        cnt+=1
    else:
        n-=1
        cnt+=1

print(cnt)

# If n's range is huge

n,k = map(int,input().split())
cnt=0

while True:
    target=(n//k)*k
    cnt+=(n-target)
    
    n=target
    if n<k:
        break
    cnt+=1
    n//=k

cnt+=(n-1)
print(cnt)