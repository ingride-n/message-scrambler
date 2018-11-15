import os, json, requests

from datetime import datetime
from datetime import date

import blackbox

web_hook_url = '[enter url here]'

today = date.today()

# Get number of days in countdown

holiday = date(today.year, 12, 18)
time_to_holiday = abs(holiday - today)
delta_t = time_to_holiday.days

# Input message

input_msg = "We are "+str(delta_t)+" days away from winter break"

# Send input message to blackbox to encode

key = blackbox.generate_key(input_msg)
msg_x = blackbox.scramble(input_msg, key)

# Save blackbox output to a file

with open('bot-messages.txt','a') as file:
	file.write(msg_x+"\t")
	file.write(key+"\t")
	file.write(str(datetime.now())+"\t")
	file.close() 

# Post message to Slack

final_msg = {'text':msg_x}
requests.post(web_hook_url,data=json.dumps(final_msg))
