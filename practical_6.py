a = str(input("Enter i for insertion sort , b for bubble sort , s for selection sort : "))
nums = [5,9,6,2,7,3,1,8,]
if a=='i':
   
    for i  in range(1,len(nums)):
        currentvalue = nums[i]
        position = i
        while(position>0 and nums[position-1] > currentvalue):
            nums[position] = nums[position-1]
            position = position-1
    nums[position] = currentvalue
    print(nums)
elif a == 'b' :
    
    def sort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1] = temp 
    sort(nums)
    print(nums)
elif a == 's':
    def sort(nums):
        for i in range(len(nums)):
            minpos = i
            for j in range(i,len(nums)):
                if nums[j] < nums[minpos]:
                    minpos=j
            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] =temp

    
    sort(nums)
    print(nums)
else:
    print("Enter valid input")
