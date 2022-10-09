import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['']
auth_token = os.environ['']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+',
                              media_url=['https://demo.twilio.com/owl.png'],
                              to='+'
                          )

print(message.sid)