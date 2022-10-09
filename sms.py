import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACae80370ac839f7515e545853177926f0']
auth_token = os.environ['']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+18123591157',
                              media_url=['https://demo.twilio.com/owl.png'],
                              to='+919919056997'
                          )

print(message.sid)