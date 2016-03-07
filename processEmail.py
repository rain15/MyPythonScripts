import smtplib

# for gmail, Sign in using App Passwords by first creating an app password for your gmail account


#conn = smtplib.SMTP('smtp.gmail.com', 587)
conn = smtplib.SMTP('mail.gmx.com', 25) #465


type(conn)
conn.ehlo()
conn.starttls()
conn.login('pythonstudent@gmx.com', 'python2015')
conn.sendmail('pythonstudent@gmx.com', 'pythonstudent@gmx.com', 'Subject: So long...\n\nDear Al, \nSo long and thanks for all the fish.\n\n-PythonLearner')

conn.sendmail('pythonstudent@gmx.com', 'pythonstudent@gmx.com', 'Subject: So long...\n\nDear Al, \nSo long and thanks for all the chicken.\n\n-PythonLearner')

conn.quit()
