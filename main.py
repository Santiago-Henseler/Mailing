# imports
from email.message import EmailMessage
import smtplib
import ssl
import time

# conifg
em = EmailMessage()
email_sender = ''
email_password = ''
context = ssl.create_default_context()

def enviarEmail(personas):

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

        smtp.login(email_sender, email_password)

        for persona in personas:

            # Set the subject and body of the email
            subject = 'Calate  las!'
            em.set_content(f"""
                    <html>
                    <body>
                        <font color="black" size="5">
                            <p><b></b> comment: "hola"</p>
    
                                 <center><button><a style="text-decoration:none" href="https://callgore.pythonanywhere.com/viewTopics/">Reply this comment</a></button></center>
                        </font>
                        <hr>           
                """, subtype='html')

            em['From'] = email_sender
            em['To'] = persona
            em['Subject'] = subject

            smtp.sendmail(email_sender, persona, em.as_string())

            time.sleep(5)
            del em['To']
            del em['Subject']
            del em['from']

def main():

    personas = ['callgoredeveloper@gmail.com', 'shenseler@fi.uba.ar']

    enviarEmail(personas)


if __name__ == "__main__":
    main()