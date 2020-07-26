t = int(input())
result = []
for i in range(t):
    n, s = map(int, input().split())
    array = list(map(int, input().split()))
    start = 0
    end = 0
    while start<=end and end<n:
        sum = 0
        for j in range(start, end+1):
            sum+=array[j]
        if sum<s:
            end+=1
        if sum>s:
            start+=1
        if sum==s:
            result.append([start+1, end+1])
            break
    if end==n:
        result.append([-1])
for r in result:
    print(*r)