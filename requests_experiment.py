#! /usr/bin/python3

import requests
import passwords

# Send the request to the httpbin with correct username/password read from the 
# passwords.py file (which should contain the correct username/password russ/test 
r = requests.get("http://0.0.0.0/basic-auth/russ/test", auth=(passwords.user, passwords.password))

# Print out the status code of the response so we can check we successfully sent
# request and got successful authentication like we expected (should be 200 to 
# indicate successful login as we used the correct username and password.)
print(r.status_code)

# Print out the body of the response, which should tell us we are authenticated 
# with username russ as we used the right username/password for username russ
print(r.text)
