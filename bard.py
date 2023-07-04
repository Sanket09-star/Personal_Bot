from bardapi import Bard
'''
For token :
Go to the google bard 
Sign in to your account 
Then go to inspect a section
Click on the application then cookies
then click on first link(https:bard.google...
find in the 'Name' column '_Secure-1PSID' in that row copy Value of that _Secure-1PSID
Paste that value in the token.
'''
token = 'xxxxxx'
bard = Bard(token=token)
response = bard.get_answer("what is ml")['content']
print(response)
