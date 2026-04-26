# inputs we need from user => using input() function

=> Number of friends/people living   
=> Total rent of Room/PG
=> Total food ordered for snacking
=> Electricity units spend
=> Charge per unit

# outputs
=> Total amount to be paid is ""
=> Each member should pay ""
 
# mistakes i did

=> not taking input in int()
=> writing everthing directly 
=> didn't handle division by zero
=> not adding a case if friends = 0
=> in if case using return instead of exit()
=> removing the self.friends == 0 as i already handle this case in try and exception method

# solutions

=> input() gives str so we need to convert it into int() for calculations
=> using class and function so we can reuse it
=> add a case if friends = 0 
=> use try and exception
=> we cannot use return as we are not inside a functionn so exit() is a best method 
=> since class is meant to be reused it is better to keep it 