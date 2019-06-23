''' 
    *     # 4 spaces 1 star
   * *    # 3 spaces 2 stars
  * * *   # 2 spaces 3 stars
 * * * *  # 1 space 4 stars
* * * * * # 0 space 5 starts
 * * * *  # 1 space 4 stars
  * * *   # 2 space 3 starts
   * *    # 3 space 2 starts
    *     # 4 spaces 1 star
 
'''    
j = 4
k = 2
l = 1
for i in range(1, 10):
    if i <= 5:
        print((" " * j) + ("* " * i))
        j -= 1
    else:    # i > 5
        print((" " * l) + ("* " * (i - k)) )
        k += 2
        l += 1
