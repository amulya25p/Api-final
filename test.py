from twilio.rest import Client
client = Client(
    "ACce76adada8f41929681a785bb386fe67", "9137a187d5f7f2b3992c5bb419aac5f4"
)

for msg in client.messages.list():
     print(f"Deleting {msg.body}")
     msg.delete()

# msg = client.messages.create(
#     to = "+919011219613",
#     from_="+15412877656",
#     body="Hello, from Python"
# )

# print(f"Created a new message: {msg.sid}")
