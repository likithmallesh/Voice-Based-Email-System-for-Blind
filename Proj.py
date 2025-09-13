from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import speech_recognition as sr
from gtts import gTTS
import pyglet
import os, time
import smtplib
import email


sst1=gTTS('Tell the senders mail:', lang='en')
print('Tell the senders mail')
ssname1=("sendermail.mp3") 
sst1.save(ssname1)
music = pyglet.media.load(ssname1,streaming = False) 
music.play()
time.sleep(music.duration)
os.remove(ssname1) 
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    r=recognizer.listen(source)
    sender1=recognizer.recognize_google(r)
    sendermail=sender1+'@gmail.com'
    # print(sendermail)
    
sst2=gTTS('Tell the senders password:', lang='en')
print('Tell the senders password')
ssname2=("senderpswd.mp3") 
sst2.save(ssname2)
music = pyglet.media.load(ssname2,streaming = False) 
music.play()
time.sleep(music.duration)
os.remove(ssname2) 
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    r=recognizer.listen(source)
    senderpswd=recognizer.recognize_google(r)
    # print(senderpswd)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sendermail,senderpswd)
        res=True
except Exception:
    res=False

if(res==True):
    log1=gTTS('Login Successfully', lang='en')
    print('Login Successfully')
    logname1=("sender.mp3") 
    log1.save(logname1)
    music = pyglet.media.load(logname1,streaming = False) 
    music.play()
    time.sleep(music.duration)
    os.remove(logname1)    
    choice=1
    while(choice):
        print("1.Send an Email")
        print("2.Search an Email in Inbox")
        print("3.View New Mails")
        print("4.Search in sent mails")
        lines = [
        "Hello, Welcome to your gmail account......",
        "How can I help you..........",
        "1.Send an Email...........",
        "2.Search an Email in Inbox......",
        "3.View New Mails.....",
        "4.Search in sent mails..............",
        "Speak the index of the operation you want to perform"
        ]

        pause_duration = 2

        processed_lines = []
        for line in lines:
            processed_lines.append(line)

        # Join processed lines into a single string
        text = " ".join(processed_lines)
        
        opr_choice=gTTS(text)
        ttsnameOpr=("operations.mp3") 
        opr_choice.save(ttsnameOpr)
        music = pyglet.media.load(ttsnameOpr, streaming = False) 
        music.play()
        time.sleep(music.duration)
        os.remove(ttsnameOpr)
        recognizer=sr.Recognizer()
        # while True:
        with sr.Microphone() as source:
            r=recognizer.listen(source) 
            try:
                print('Printing the operation to be performed')
                opr=recognizer.recognize_google(r,language='en') 
                print(opr)
                # opr=3
                if(opr=='1' or opr=="One" or opr=="one"):
                    number=1
                    print(number)
                elif(opr=='2' or opr=="tu" or opr=="Tu" or opr=="two"):
                    number=2
                    print(number)
                elif opr=='3' or opr=="three" or opr=="Three" or opr=="tree" or opr=="free" or opr=="thee":
                    number=3
                    print(number)
                elif opr=='4' or opr=="four" or opr=="Four" or opr=="for" or opr=="Pur":
                    number=4
                    print(number)
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please speak again.")
            except sr.RequestError as e:
                print("Sorry, an error occurred while recognizing your speech.")
            
            match number:

                case 1:  
                    print("Senders mail: muskantest12@gmail.com") 
                #Converting text into speech
                    tts3=gTTS('Tell the recievers mail:', lang='en')
                    ttsname3=("recieve.mp3") 
                    tts3.save(ttsname3)
                    music = pyglet.media.load(ttsname3,streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname3) 

                    with sr.Microphone() as source:
                        r=recognizer.listen(source)
                        reciv1=recognizer.recognize_google(r)
                        reciv2=reciv1.lower()
                        reciv3=reciv2.replace(" ","")
                        reciever=reciv3+"@gmail.com"
                        print('Receivers Mail',reciever)
                        
                    tts=gTTS('Speak subject of the mail and say subject done for indicating subject completion. Then speak the body part of mail:', lang='en')
                    ttsname=("msg.mp3") 
                    tts.save(ttsname)
                    music = pyglet.media.load(ttsname, streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsname)    
                    
                    with sr.Microphone() as source:
                        print('Clearing background noise..')
                        recognizer.adjust_for_ambient_noise(source,duration=1)
                        print('Waiting for your message...')
                        recordedaudio=recognizer.listen(source)
                        print('Done recording')
                    try:
                        print('Printing the message..')
                        text=recognizer.recognize_google(recordedaudio,language='en-US')
                        subject,body = text.split('subject done', 1)
                        print(f"Subject: {subject}")
                        print(f"Body: {body}")
                        
                    except Exception as ex:
                        print(ex)
                        
                    recordSender='muskantest12@gmail.com'
                    recordPswd='qnuumxpjdhqjgzhd'

                    #Creating a new message
                    msg = MIMEMultipart()
                    msg['From'] = recordSender
                    msg['To'] = reciever
                    msg['Subject'] =subject
                    msg.attach(MIMEText(body, 'plain'))

                    # Connecting to the SMTP server to send the email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(recordSender,recordPswd)
                        server.sendmail(recordSender,reciever,msg.as_string())
                    print('Email successfully sent')
                    ss3=gTTS('Email successfully sent:', lang='en')
                    ssname3=("success.mp3") 
                    ss3.save(ssname3)
                    music = pyglet.media.load(ssname3,streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ssname3)  
            
                case 2:
                    recordSender='muskantest12@gmail.com'
                    recordPswd='qnuumxpjdhqjgzhd'
                    # Connecting to the SMTP server to send the email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(recordSender,recordPswd)

                    imap_server = "imap.gmail.com"
                    # Log in to IMAP server
                    imap_connection = imaplib.IMAP4_SSL(imap_server)
                    login=imap_connection.login(recordSender, recordPswd)
                    imap_connection.select("INBOX")

                    print("Tell the search criterion for searching the mail")
                    search_play=gTTS('Tell the search criterion for searching the mail:', lang='en')
                    ttsnameSR=("criterion.mp3") 
                    search_play.save(ttsnameSR)
                    music = pyglet.media.load(ttsnameSR, streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsnameSR)
                        
                    #To recognize the voice for search criterion input
                    recognizer=sr.Recognizer()
                    with sr.Microphone() as source:
                        r=recognizer.listen(source) 
                        print('Printing the search criterion..')
                        search_criterion=recognizer.recognize_google(r,language='en') 
                        print(search_criterion)


                    # Search for emails matching criterion
                    imap_response, email_ids = imap_connection.search(None, f"TEXT \"{search_criterion}\"")
                    if imap_response == 'OK':
                        email_id = email_ids[0].split()
                        
                    if len(email_id)==0:
                        print('There are no mails based on your search criterion')
                        mail_res=gTTS('There are no mails based on your search criterion', lang='en')
                        ttsnameRes=("no_search.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                    else:
                        print('The mails related to your search are: ')
                        mail_res=gTTS('The mails related to your search are:', lang='en')
                        ttsnameRes=("mails.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                        # print("The mails related to your search are:")

                        for i, id in enumerate(email_id):
                            typ, data =imap_connection.fetch(id, '(BODY.PEEK[])')
                            msg = email.message_from_bytes(data[0][1])
                            a=f"{i}: {msg['Subject']}"
                            # ,'which came on date',msg['Date']
                            print(a)
                            tts6=gTTS(text=a,lang='en')
                            ttsname6=("search.mp3") 
                            tts6.save(ttsname6)
                            music = pyglet.media.load(ttsname6,streaming = False) 
                            music.play()
                            time.sleep(music.duration)
                            os.remove(ttsname6) 

                        #Choose index of mail you want to read
                        mail_index=gTTS('Enter the index of the email you want to read: ', lang='en')
                        ttsnameIndex=("index.mp3") 
                        mail_index.save(ttsnameIndex)
                        music = pyglet.media.load(ttsnameIndex, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameIndex)

                        #Speak index of mail you want to read
                        recognizer=sr.Recognizer()
                        with sr.Microphone() as source:
                            r=recognizer.listen(source) 
                            print('Printing the email index..')
                            chosen_ind=recognizer.recognize_google(r,language='en') 
                            print(chosen_ind)
                            if(chosen_ind=='one' or chosen_ind=='One' or chosen_ind=='1'):
                                chosen_index=1
                            elif(chosen_ind=='two' or chosen_ind=='Tu' or chosen_ind=='2' or chosen_ind=='Two'):
                                chosen_index=2
                            elif(chosen_ind=='three' or chosen_ind=='tree' or chosen_ind=='3' or chosen_ind=='Three'):
                                chosen_index=3
                            elif(chosen_ind=='zero' or chosen_ind=='0' or chosen_ind=='Zero' or chosen_ind=='Jero'):
                                chosen_index=0
                            elif(chosen_ind=='four' or chosen_ind=='Four' or chosen_ind=='4' or chosen_ind=='for'):
                                chosen_index=4
                            elif(chosen_ind=='five' or chosen_ind=='Five' or chosen_ind=='5'):
                                chosen_index=5
                            elif(chosen_ind=='six' or chosen_ind=='Six' or chosen_ind=='6'):
                                chosen_index=6
                            elif(chosen_ind=='seven' or chosen_ind=='Seven' or chosen_ind=='7'):
                                chosen_index=7
                            elif(chosen_ind=='eight' or chosen_ind=='Eight' or chosen_ind=='8'):
                                chosen_index=8
                            elif(chosen_ind=='Nine' or chosen_ind=='nine' or chosen_ind=='9'):
                                chosen_index=9   
                        # chosen_index = int(input("Enter the index of the email you want to read: "))
                        chosen_msg_id = email_id[chosen_index]

                        imap_response, email_data = imap_connection.fetch(chosen_msg_id, "(RFC822)")
                        if imap_response != "OK":
                            print(f"Error: {imap_response}")
                            # exit()

                        # Parse email message data
                        email_message = email.message_from_bytes(email_data[0][1])
                        email_from = email_message["From"]
                        email_subject = email_message["Subject"]
                        email_date = email_message['Date']
                        if email_message.is_multipart():
                                for part in email_message.get_payload():
                                    if part.get_content_type() == 'text/plain':
                                        message_body = part.get_payload(decode=True).decode('utf-8')
                                        print(f"Message Body1: {message_body}")
                        else:
                            message_body = email_message.get_payload(decode=True).decode('utf-8')
                            print(f"Message Body2: {message_body}")


                        # Read email contents to user
                        tts = gTTS(f"The mail is from {email_from}, with subject {email_subject}. The email says: {message_body}")
                        mediaemail=("email.mp3")
                        tts.save(mediaemail)
                        music = pyglet.media.load(mediaemail, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(mediaemail)

                case 3:
                    recordSender='muskantest12@gmail.com'
                    recordPswd='qnuumxpjdhqjgzhd'
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(recordSender,recordPswd)
                    imap_server = "imap.gmail.com"
                    # Log in to IMAP server
                    imap_connection = imaplib.IMAP4_SSL(imap_server)
                    login=imap_connection.login(recordSender, recordPswd)
                    imap_connection.select("INBOX")
                    # Search for emails matching criterion
                    imap_response, email_ids = imap_connection.search(None, '(UNSEEN)')
                    if imap_response == 'OK':
                        email_id = email_ids[0].split()
                        
                    if len(email_id)==0:
                        print('There are no new mails')
                        mail_res=gTTS('There are no new mails', lang='en')
                        ttsnameRes=("no_new.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                        # print("There are no new mails")
                        # exit()
                    else:
                        print('The new mails in your account are')
                        mail_res=gTTS('The new mails on your account are:', lang='en')
                        ttsnameRes=("mails_new.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                        # print("The mails related to your search are:")

                        for i, id in enumerate(email_id):
                            typ, data =imap_connection.fetch(id, '(BODY.PEEK[])')
                            msg = email.message_from_bytes(data[0][1])
                            a=f"{i}: {msg['Subject']}"
                            print(a)
                            # ,'which came on date',msg['Date']
                            tts6=gTTS(text=a,lang='en')
                            ttsname6=("search_new.mp3") 
                            tts6.save(ttsname6)
                            music = pyglet.media.load(ttsname6,streaming = False) 
                            music.play()
                            time.sleep(music.duration)
                            os.remove(ttsname6) 

                        #Choose index of mail you want to read
                        print('Enter the index of the email you want to read')
                        mail_index=gTTS('Enter the index of the email you want to read: ', lang='en')
                        ttsnameIndex=("index_new.mp3") 
                        mail_index.save(ttsnameIndex)
                        music = pyglet.media.load(ttsnameIndex, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameIndex)

                        #Speak index of mail you want to read
                        recognizer=sr.Recognizer()
                        with sr.Microphone() as source:
                            r=recognizer.listen(source) 
                            print('Printing the email index..')
                            chosen_ind=recognizer.recognize_google(r,language='en') 
                            print(chosen_ind)
                            if(chosen_ind=='one' or chosen_ind=='One' or chosen_ind=='1'):
                                chosen_index=1
                            elif(chosen_ind=='two' or chosen_ind=='Tu' or chosen_ind=='2' or chosen_ind=='Two'):
                                chosen_index=2
                            elif(chosen_ind=='three' or chosen_ind=='tree' or chosen_ind=='3' or chosen_ind=='Three'):
                                chosen_index=3
                            elif(chosen_ind=='zero' or chosen_ind=='0' or chosen_ind=='Zero' or chosen_ind=='Jero'):
                                chosen_index=0
                            elif(chosen_ind=='four' or chosen_ind=='Four' or chosen_ind=='4' or chosen_ind=='for'):
                                chosen_index=4
                            elif(chosen_ind=='five' or chosen_ind=='Five' or chosen_ind=='5'):
                                chosen_index=5
                            elif(chosen_ind=='six' or chosen_ind=='Six' or chosen_ind=='6'):
                                chosen_index=6
                            elif(chosen_ind=='seven' or chosen_ind=='Seven' or chosen_ind=='7'):
                                chosen_index=7
                            elif(chosen_ind=='eight' or chosen_ind=='Eight' or chosen_ind=='8'):
                                chosen_index=8
                            elif(chosen_ind=='Nine' or chosen_ind=='nine' or chosen_ind=='9'):
                                chosen_index=9   
                        # chosen_index = int(input("Enter the index of the email you want to read: "))
                        chosen_msg_id = email_id[chosen_index]

                        imap_response, email_data = imap_connection.fetch(chosen_msg_id, "(RFC822)")
                        if imap_response != "OK":
                            print(f"Error: {imap_response}")
                            # exit()

                        # Parse email message data
                        email_message = email.message_from_bytes(email_data[0][1])
                        email_from = email_message["From"]
                        email_subject = email_message["Subject"]
                        email_date = email_message['Date']
                        if email_message.is_multipart():
                                for part in email_message.get_payload():
                                    if part.get_content_type() == 'text/plain':
                                        message_body = part.get_payload(decode=True).decode('utf-8')
                                        print(f"Message Body1: {message_body}")
                        else:
                            message_body = email_message.get_payload(decode=True).decode('utf-8')
                            print(f"Message Body2: {message_body}")


                        # Read email contents to user
                        tts = gTTS(f"The mail is from {email_from}, with subject {email_subject}. The email says: {message_body}")
                        mediaemail=("email.mp3")
                        tts.save(mediaemail)
                        music = pyglet.media.load(mediaemail, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(mediaemail)

                case 4:
                    recordSender='muskantest12@gmail.com'
                    recordPswd='qnuumxpjdhqjgzhd'
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                        server.login(recordSender,recordPswd)
                    
                    imap_server = "imap.gmail.com"
                    # Log in to IMAP server
                    imap_connection = imaplib.IMAP4_SSL(imap_server)
                    login=imap_connection.login(recordSender, recordPswd)
                    imap_connection.select('"[Gmail]/Sent Mail"')
                    # Search for emails matching criterion
                    print('Tell the search criterion for searching the mail in sent box')
                    search_play=gTTS('Tell the search criterion for searching the mail in sent box:', lang='en')
                    ttsnameSR=("criterion_sent.mp3") 
                    search_play.save(ttsnameSR)
                    music = pyglet.media.load(ttsnameSR, streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsnameSR)
                        
                    #To recognize the voice for search criterion input
                    recognizer=sr.Recognizer()
                    with sr.Microphone() as source:
                        r=recognizer.listen(source) 
                        print('Printing the search criterion..')
                        search_criterion=recognizer.recognize_google(r,language='en') 
                        print(search_criterion)


                    # Search for emails matching criterion
                    imap_response, email_ids = imap_connection.search(None, f"TEXT \"{search_criterion}\"")
                    if imap_response == 'OK':
                        email_id = email_ids[0].split()

                    if len(email_id)==0:
                        print('There are no sent mails matching your search criterion')
                        mail_res=gTTS('There are no sent mails matching your search criterion', lang='en')
                        ttsnameRes=("no_new.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                        # print("There are no new mails")
                        # exit()
                    else:
                        print('The sent mails in your account based on your search criterion are:')
                        mail_res=gTTS('The sent mails in your account based on your search criterion are:', lang='en')
                        ttsnameRes=("mails_new.mp3") 
                        mail_res.save(ttsnameRes)
                        music = pyglet.media.load(ttsnameRes, streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsnameRes)
                    # print("The mails related to your search are:")

                    for i, id in enumerate(email_id):
                        typ, data =imap_connection.fetch(id, '(BODY.PEEK[])')
                        msg = email.message_from_bytes(data[0][1])
                        a=f"{i}: {msg['Subject']}"
                        print(a)
                        # ,'which came on date',msg['Date']
                        tts6=gTTS(text=a,lang='en')
                        ttsname6=("search_new.mp3") 
                        tts6.save(ttsname6)
                        music = pyglet.media.load(ttsname6,streaming = False) 
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsname6) 

                    #Choose index of mail you want to read
                    mail_index=gTTS('Enter the index of the email you want to read: ', lang='en')
                    ttsnameIndex=("index_new.mp3") 
                    mail_index.save(ttsnameIndex)
                    music = pyglet.media.load(ttsnameIndex, streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(ttsnameIndex)

                    #Speak index of mail you want to read
                    recognizer=sr.Recognizer()
                    with sr.Microphone() as source:
                        r=recognizer.listen(source) 
                        print('Printing the email index..')
                        chosen_ind=recognizer.recognize_google(r,language='en') 
                        print(chosen_ind)
                        if(chosen_ind=='one' or chosen_ind=='One' or chosen_ind=='1'):
                                chosen_index=1
                        elif(chosen_ind=='two' or chosen_ind=='Tu' or chosen_ind=='2' or chosen_ind=='Two'):
                            chosen_index=2
                        elif(chosen_ind=='three' or chosen_ind=='tree' or chosen_ind=='3' or chosen_ind=='Three'):
                            chosen_index=3
                        elif(chosen_ind=='zero' or chosen_ind=='0' or chosen_ind=='Zero' or chosen_ind=='Jero'):
                            chosen_index=0
                        elif(chosen_ind=='four' or chosen_ind=='Four' or chosen_ind=='4' or chosen_ind=='for'):
                            chosen_index=4
                        elif(chosen_ind=='five' or chosen_ind=='Five' or chosen_ind=='5'):
                            chosen_index=5
                        elif(chosen_ind=='six' or chosen_ind=='Six' or chosen_ind=='6'):
                            chosen_index=6
                        elif(chosen_ind=='seven' or chosen_ind=='Seven' or chosen_ind=='7'):
                            chosen_index=7
                        elif(chosen_ind=='eight' or chosen_ind=='Eight' or chosen_ind=='8'):
                            chosen_index=8
                        elif(chosen_ind=='Nine' or chosen_ind=='nine' or chosen_ind=='9'):
                            chosen_index=9   
                        # chosen_index=eval(chosen_ind)
                    # chosen_index = int(input("Enter the index of the email you want to read: "))
                    chosen_msg_id = email_id[chosen_index]

                    imap_response, email_data = imap_connection.fetch(chosen_msg_id, "(RFC822)")
                    if imap_response != "OK":
                        print(f"Error: {imap_response}")
                        # exit()

                    # Parse email message data
                    email_message = email.message_from_bytes(email_data[0][1])
                    email_from = email_message["From"]
                    email_subject = email_message["Subject"]
                    email_date = email_message['Date']
                    if email_message.is_multipart():
                            for part in email_message.get_payload():
                                if part.get_content_type() == 'text/plain':
                                    message_body = part.get_payload(decode=True).decode('utf-8')
                                    print(f"Message Body1: {message_body}")
                    else:
                        message_body = email_message.get_payload(decode=True).decode('utf-8')
                        print(f"Message Body2: {message_body}")


                    # Read email contents to user
                    tts = gTTS(f"The mail is from {email_from}, with subject {email_subject}. The email says: {message_body}")
                    mediaemail=("email.mp3")
                    tts.save(mediaemail)
                    music = pyglet.media.load(mediaemail, streaming = False) 
                    music.play()
                    time.sleep(music.duration)
                    os.remove(mediaemail)

        # choiceAud=int(input("Do you want to perform more operations: 1/0"))
            choiceAud=gTTS('Do you want to perform more operations...Say one to continue and zero to exit', lang='en')
            ttsnameChoice=("index_choice.mp3") 
            choiceAud.save(ttsnameChoice)
            music = pyglet.media.load(ttsnameChoice, streaming = False) 
            music.play()
            time.sleep(music.duration)
            os.remove(ttsnameChoice)

            recognizer=sr.Recognizer()
            with sr.Microphone() as source:
                r=recognizer.listen(source) 
                print('Printing the users choice....')
                opr1=recognizer.recognize_google(r,language='en') 
                if(opr1=='1' or opr1=="One" or opr1=="one"):
                    choice=1
                    print(choice)
                else:
                    choice=0
else:
    log2=gTTS('Invalid Credentials.Login again', lang='en')
    logname2=("sender.mp3") 
    log2.save(logname2)
    music = pyglet.media.load(logname2,streaming = False) 
    music.play()
    time.sleep(music.duration)
    os.remove(logname2) 