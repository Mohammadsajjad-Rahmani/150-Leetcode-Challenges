def BestTimeToBuyAndSell_II(prices):
        
    if not prices:
        return 0
    
    max_profit = 0
    
    for i in range(1, len(prices)):
        
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1] 
        
                
    return max_profit


print(BestTimeToBuyAndSell_II([7,1,5,3,6,4]))  # Output: 7