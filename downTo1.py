# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:05:28 2021
@author: Richard Paglia

Down to 1
"""
count = 0                                       # Counter for steps
n = int(input('Enter a number: '))              # Receive initial number

while n <= 0:                                   # Error checking for positive integer
    print('\033[0;31;mError: Must be a positive integer, try again!')
    print()                                     # \033[0;31;m - Adds color to text
    n = int(input('\033[0;0;m Enter a number: '))
                                                # \033[0;0;m - Resets to original color
while n > 1:
    if (n % 2) == 0:                            # Even number
        print(int(n),end=(', '), flush=True)    # Print on one line
        n = n/2       
        count += 1                              # Increase counter
    else:                                       # Odd number 
        print(int(n),end=(', '), flush=True)    # Print on one line
        n = 3*n+1        
        count += 1                              # Increase counter
    
if n == 1:
    print(int(n))
    print('\n\033[0;36;mIt took', count, 'tries to get down to 1. \033[0;0;m')
