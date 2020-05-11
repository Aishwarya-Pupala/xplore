

import re

email="ashpupala12@gmail.com"

x=re.findall("@+.{1}com",email)

if x:
    print("valid email id")
else:
    print("invalid email id")
    
    
    
