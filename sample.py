from os import name
import yagmail,time
from datetime import datetime
now = datetime.now()
#print(now.strftime("%H-%M"))
while True:
    try:
    #initializing the server connection
        yag = yagmail.SMTP(user='shammithebot@gmail.com', password='Soorajsivadas767')
        #sending the email
        yag.send(to='sjts007@gmail.com', subject=f'Hi from heroku', contents=f'The time is {now}')
        print(f"Email sent successfully to sjts007@gmail.com")
    except:
        print(f"Error, email was not sent to sjts007@gmail.com")
    time.sleep(10)
