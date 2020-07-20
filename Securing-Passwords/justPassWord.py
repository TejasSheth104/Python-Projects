
# merge - 
# 1. passKeeperNManager
# 2. pswd_gen
# 3. pswd_validator

# 1. asks to enter title and password, 
# at the time of inserting password, asks if want to try the pswd_gen(),
#       ``` if yes goes to the function, else BOOM.
# after entering the password of our choice or using the generator,
# asks if want to validate the password I entered, and not what was generated.
#       ``` if yes goes to the pswd_validator() function, else BOOM

from passKeeperNManager import passKeeperNManager
from pswd_gen import pswd_gen
from pswd_validator import pswd_validator



