import twilio
#print(twilio.__version__)

from twilio.rest import Client
#from moduleName.folder import class name

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb1a2f4660f8e0c364ae7f8459cb79519'
auth_token = '40b18f174aadf8d1bf4496ebf7e879fd'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+66 91 429 9144", 
    from_="+18433218002",
    body="Khwandao Issara (student ID:6005005902)"
)

print(message.sid)