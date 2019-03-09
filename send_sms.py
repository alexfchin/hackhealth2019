from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACdacdabd3923e0062efc6bceae3b02a11"
# Your Auth Token from twilio.com/console
auth_token  = "70a3535b5e078d10afe48b3f825c630c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12016388380",
    from_="+19733580677",
    body="Hello from Python!")

print(message.sid)