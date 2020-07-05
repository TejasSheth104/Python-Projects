# main purpose - 
# automatic replies to the list of peoples - entered manually (or received through google forms.),
# sending reply mail commonly, marked as BCC.

# adjust your Gmail account’s security settings to allow access from your Python code, 
# and because there’s a chance you might accidentally expose your login details.

import ssl
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# mail subject input - 
def mail_subject():
    subject = input('Enter the Subject - ')
    return subject


# mail body input - 
def mail_body():
    print('SEND TO - \n1.) Write Now, Here Itself.\n2.) A \'.txt\' File.')
    try:
        choice = int(input('Enter - '))
        if 1 > choice > 2:
            print('InValid Input - Default => 1. Selected')
            choice = 1
    except TypeError:
        print('InValid Type - Default => 1. Selected')
        choice = 1
    if choice == 1:
        body_contents = input('Enter the Body - ')
    elif choice == 2:
        body_contents = ''
        # choose a file and open it, read it.
        print('File Should be \'.txt\',\nFile Location must be where \'.py\' file is\nElse Enter complete file address.')
        filename = input('Enter File Name/ Location - ')
        filehandle = open(filename)
        for file_contents in filehandle:
            body_contents += file_contents
        body_contents += signature()
    return body_contents


# senders list
def send_to():
    senders_list = list()
    print('SEND TO - \n1.) EveryOne in the List\n2.) Only Selected.')
    try:
        choice = int(input('Enter - '))
        if 1 > choice > 2:
            print('InValid Input - Default => 1. Selected')
            choice = 1
    except TypeError:
        print('InValid Type - Default => 1. Selected')
        choice = 1
    mailId_filename = input('Enter File Name/ Location - ')
    mailId_handle = open(mailId_filename)

    if choice == 1:
        # select all the names.
        senders_list = list()
        for mailIds in mailId_handle:
            mailIds = mailIds.split(' ')
            senders_list.append(mailIds)
    elif choice == 2:
        # iterate through the list and select one by one.
        for mailIds in mailId_handle:
            mailIds = mailIds.split(' ')
            print('Do you want to Select =', mailIds)
            print(' 1 for \'YES\'\n 0 for \'NO\'')
            try:
                option = int(input('Enter - '))
                if 0 > option > 1:
                    print('InValid Input - Default => 0. Selected')
                    option = 0
            except TypeError:
                print('InValid Type - Default => 0. Selected')
                option = 0
            
            if option == 1:
                senders_list.append(mailIds)
        # list thus formed to send mail to.
    
    print('SEND AS - \n1.) To\n2.) CC\n3.) BCC')
    try:
        choice = int(input('Enter - '))
        if 1 > choice > 3:
            print('InValid Input - Default => 3. Selected')
            choice = 3
    except TypeError:
        print('InValid Type - Default => 2. Selected')
        choice = 2
    if choice == 1:
        send_all_as = 'To'
    elif choice == 2:
        send_all_as = 'CC'
    elif choice == 3:
        send_all_as = 'BCC'
    return senders_list, send_all_as


def gmail_login():
    u_name = input('Enter your G-Mail ID [xyz@abc.com]- ')
    try:
        pswd = getpass.getpass()
    except Exception as error:
        print('ERROR - ', error)
        print('\n\nInValid Attempt.\n\tTRY AGAIN.')
        exit(-1)
    return u_name, pswd


def signature():
    salutation = input('Enter Salutation - ')
    name = input('Enter your Name - ')
    position = input('Enter your Positon - ')
    contact = input('Enter your Contact Number - ')
    signature_contents = '\n'+ salutation + ',\n' + name + '\n' + position + '\n' + contact
    return signature_contents


# main starts here - 
userid, password = gmail_login()
receivers, send_type = send_to()

main_msg = MIMEMultipart()

main_msg['From'] = userid
main_msg[send_type] = ", ".join(str(receivers)) # comma seperated string.
main_msg['Subject'] = mail_subject()
body = mail_body()
main_msg.attach(MIMEText(body, 'plain'))

# SMTP commands. = SIMPLE MAIL TRANSFER PROTOCOL.
text = main_msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(userid, password)
server.sendmail(userid, 'to', text)
server.quit()

