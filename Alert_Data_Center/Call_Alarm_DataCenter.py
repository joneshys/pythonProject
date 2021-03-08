import imaplib
import email
from email.header import decode_header
from twilio.rest import Client


username = "quipuxpruebatest01@gmail.com"
password = "cL6EZfzQ8IUyA7qccw3TVGS9XU1xYf5W"


imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
imap.select("INBOX")

#status, messages = imap.search(None, 'FROM "jose.benitez@quipux.com"')
# status, messages = imap.search(None, "ALL")
status, messages = imap.search(None, 'SUBJECT "TEMPERATURE ALARM"')
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')

# convert messages to a list of email IDs
messages = messages[0].split(b' ')

try:
    for mail in messages:
        msg = imap.fetch(mail, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                print("Deleting", subject)
        imap.store(mail, "+FLAGS", "\\Deleted")
    imap.expunge()
    imap.close()
    imap.logout()
    account_sid = 'AC367d637e1d886ef6f185bb87f9ac12db'
    auth_token = '61a1a156824b7b9c98f812b7cfd64b10'
    client = Client(account_sid, auth_token)
    #call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',to='+573004180554',from_='+12512835176')
    call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='+573157187039', from_='+12512835176')
    #call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to='+573128604221', from_='+12512835176')
    print(call.sid)
except:
    print('No hay correos')