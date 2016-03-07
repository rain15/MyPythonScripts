import imapclient, pyzmail

#for gmail, Sign in using App Passwords
#conn = imapclient.IMAPClient('imap.gmx.com', ssl=True)
#conn.login('pythonstudent@gmx.com', 'python2015')

conn = imapclient.IMAPClient('imap.gmx.com', ssl=True)
conn.login('pythonstudent@gmx.com', 'python2015')
conn.select_folder('INBOX', readonly = True)

#date below had to be exact format. 2 digits if it's a number less than 10
UIDs = conn.search(['SINCE 02-Feb-2016'])

# 47474 is an example of the UID that is in the result of list of UIDs from above statement
rawMessage = conn.fetch([47474], ['BODY', 'FLAGS'])

# b'BODY[] is part of the result in rawMessage from above line
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])

message.get_subject()
message.get_addresses('from')

message.get_addresses('to')

message.get_addresses('bcc')

message.text_part

message.html_part

message.text_part.getpayload().decode('UTF-8')

message.text_part.charset

conn.list_folder() # 3rd item in tuple list returned is folder name.

conn.delete_message([47474]) # CAN SEND MULTIPLE UIDs

conn.logout()

