#import necessary libraries
import itertools
import string
import time

#define the brute force function
def brute_force(length = 4):
   chars = string.ascii_lowercase + string.digits  #lowercase letters and digits 
   attempts = 0   #attempt counter
   s_time = time.time() #time counter
   
   for password_length in range(1, length+1):
      for guess in itertools.product(chars, repeat = password_length):     #Create all possible combinations of 'chars' with given 'password_length'
         attempts += 1
         guess = ''.join(guess)  # Convert tuple to string
         print(f"Trying: {guess}")
         
         # Check if guess matches the real password
         if guess == real_password:
            e_time = time.time()
            return True, guess, attempts, e_time - s_time   # Return success info
         
   return False, None, attempts, time.time() - s_time    # Return failure info

real_password = "12p"      # Set the real password

success, password, attempts, time_takes = brute_force(3)    # Call the brute force function

# Check result and print output
if success:
   print(f"\npassword found : {password}")
   print(f"Total attempts : {attempts}")
   print(f"Time taken : {time_takes}")
   
else:
   print("\nPassword not found")