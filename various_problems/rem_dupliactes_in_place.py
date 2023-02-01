"""Better way than removeDupliacates_2"""
def removeDuplicates_1(nums):
    i=0
    for j in range(1,len(nums)):
        if(nums[i]==nums[j]):
            continue
        else:
            nums[i+1]=nums[j]
            i=i+1
    print(nums)    
    return i+1

print(removeDuplicates_1([1,1,1,2,2,2,3,4,4]))    


def removeDuplicates_2(nums):
    length = len(nums)
    k = 0
    i = 0
    while i<length-1:
        if nums[i] == nums[i+1]:
            k += 1
            for j in range(i+1,length-1):
                nums[j],nums[j+1] = nums[j+1],nums[j]
            length -= 1
        else:
            i += 1
    print(nums)        
    return len(nums) - k    

print(removeDuplicates_2([0,1,1,2,3,3,4,4,4,4,5,5]))    


