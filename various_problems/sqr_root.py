def square_root(n,k):

    i=1
    res=1
    if(n==0 or n==1):
        return n

    while(res<=n):
        i+=1
        res=i*i

    answer=i-1
    incr = 0.1
    for j in range(0,k):
        while(answer*answer<=n):
            answer+=incr

        answer-=incr
        incr/=10

    return answer

print(square_root(9,4))
