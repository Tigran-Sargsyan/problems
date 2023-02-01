def sqrtt(n):
    root = 1
    while not guess_enough(root,n):
        root = improve(root,n)
    return root

def guess_enough(value,target):
    if abss(value ** 2 - target) < 0.00001:
        return True
    else:
        return False

def abss(num):
    if num>0:
        return num
    else:
        return -num

def improve(root,target):
    return (root+target/root) / 2

res = sqrtt(4)
print(res)