from twilio.rest import Client
from config

# Your Account SID from twilio.com/console
account_sid = config.twilio_sid
# Your Auth Token from twilio.com/console
auth_token = config.twilio_secret

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12016388380",
    from_="+19733580677",
    body="Hello from Python!")

print(message.sid)
