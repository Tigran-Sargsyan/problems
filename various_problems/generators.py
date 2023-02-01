def fact():
    init = 1
    res = 1 
    while init<20:
        res = res * init
        yield res
        init += 1

f = fact()
print(list(f))

def fact2():
    res = 1
    lst = [] 
    for i in  range(1,21):
        res *= i
        lst.append(res)
    return lst 

print(fact2())       