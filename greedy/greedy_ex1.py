# 큰 수의 법칙 (그리디)

n,m,k=map(int,input().split())

arr=list(map(int,input().split()))

arr.sort(reverse=True)

total=0
cnt = 0 # 더해지는 횟수 세기용도
result = 0 # 큰 수의 결과

while total<m:
    
    if cnt>=k:
        result+=arr[1]
        cnt=0
        total+=1
        continue
    
    total+=1
    result+=arr[0]
    cnt+=1
        
print(result)