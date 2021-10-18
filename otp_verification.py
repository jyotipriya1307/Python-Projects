import random
from twilio.rest import Client

reciever="+91" + input("Enter the reciever's number=")

otp = random.randint(1000,9999)
account_sid='ACdaf3c5de76e84f542fbc9bdb9c3accd4'
auth_token= '292c0c146fbf95a97a97d70651d1f70a'
client=Client(account_sid,auth_token)


message=client.messages \
              .create(
                  #body='Your OTP is='+str(otp),
                  body='hello pintu',
                  from_='+19705192187',
                  to=reciever
               )
req_otp=input("Enter the otp received on your phone=")

if str(req_otp) == str(otp):
    print("Approved")
    
else:
    print("Not Approved")

    
