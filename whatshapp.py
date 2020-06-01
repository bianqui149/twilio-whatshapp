import os
from twilio.rest import Client 
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) 
account_sid = os.getenv("TWILIO_ACCOUNT_SID") 
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
myphone = os.getenv("TWILIO_MY_PHONE") 
twilio = os.getenv("TWILIO_PHONE")
body_message = 'Twilio Message'
client = Client(account_sid, auth_token) 
message = client.messages.create( 
                              from_='whatsapp: ' + twilio,  
                              body= body_message,      
                              to='whatsapp: ' + myphone
                          ) 
# print message output
print(message.sid)
