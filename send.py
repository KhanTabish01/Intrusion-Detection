from twilio.rest import Client

account_sid = 'AC007ce6b095c9b8235b6981032f9cee1b'
auth_token = '996cb2e34c64021c7bc1301d5a7905a9'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='ALERT!!! Intrution Detected ',
  to='whatsapp:+919326835044'
)

print(message.sid)