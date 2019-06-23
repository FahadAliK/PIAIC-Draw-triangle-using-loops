''' 
     *      # 5 spaces and 1 star
    * *     # 4 spaces and 2 stars      
   * * *    # 3 spaces and 3 stars      
  * * * *   # 2 spaces and 4 starts                              number of rows = 9, 11, 13, 15, .....
 * * * * *  # 1 space and 5 stars  
* * * * * * # 0 space and 6 stars    
 * * * * *  # 1 space and 5 stars    
  * * * *   # 2 spaces and 4 stars  
   * * *    # 3 spaces and 3 stars    
    * *     # 4 spaces and 2 stars    
     *      # 5 spaces and 1 star
'''    
number_of_rows = 15
j = ((number_of_rows + 1) // 2) - 1
k = 2
l = 1
for i in range(1, number_of_rows + 1):
    if i <= (number_of_rows + 1) / 2:
        print( (" " * j) + ("* " * i) )
        j -= 1
    else: # i > 6
        print( (" " * l ) + ("* " * (i - k) ) )
        k += 2
        l += 1
