def jump_game(nums):
    
    max_reach = 0
    
    for i in range(0,len(nums)):
        
        if i > max_reach:
            return False
            
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return False

       
        
        




print(jump_game([3,2,1,0,4])) #False