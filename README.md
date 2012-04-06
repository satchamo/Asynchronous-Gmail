Summary
=
Send an email using Gmail as the SMTP server. Because of the high cost of
setting up the connection, the email is sent asynchronously. It is configured
to use Django's settings file by default.

Setup
=
In a Django environment:
-
In your settings.py file, create two variables:
    GMAIL_USERNAME = 'username@gmail.com'
    GMAIL_PASSWORD = 'your_PaSsWoRd'

Non-Django envrionment:
-
Remove `from django.conf import settings` from gmail.py, and set the
`GMAIL_USERNAME` and `GMAIL_PASSWORD` variables.


Example Usage
=
import gmail
to = "someone@example.com"
subject = "Hey!"
body = "Have a great day"
html = "Have a <strong>great</strong> day"
gmail.send(to, subject, body, html)

