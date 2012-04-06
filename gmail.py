import threading
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# If you want to use this without Django, remove the below line,
# and set the username and password
from django.conf import settings
GMAIL_USERNAME = settings.GMAIL_USERNAME
GMAIL_PASSWORD = settings.GMAIL_PASSWORD

class GmailThread(threading.Thread):
    def __init__(self, to, subject, body, html):
        self.to = to
        self.subject = subject
        self.body = body
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
      """ Send an email using Gmail as the SMTP server """
      message = MIMEMultipart('alternative')
      message['From'] = GMAIL_USERNAME
      message['To'] = self.to
      message['Subject'] = self.subject
      message.attach(MIMEText(self.body))
      if self.html:
          message.attach(MIMEText(self.html, 'html'))

      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.ehlo()
      server.starttls()
      server.ehlo()
      
      server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
      server.sendmail(GMAIL_USERNAME, self.to, message.as_string())
      
      server.close()


def send(to, subject, body, html=None):
    """Send an email using Gmail as the SMTP server, asynchronously"""
    e = GmailThread(to, subject, body, html)
    e.start()

