import smtplib
# from twilio.rest import Client

TWILIO_SID = "AC131eb0386f8aa5ac4e626c240320ada8"
TWILIO_AUTH_TOKEN = "8fe702ee69fea766270bf374820b7745"
TWILIO_VIRTUAL_NUMBER = "+19705783846"
TWILIO_VERIFIED_NUMBER = "+919051095101"
EMAIL = "arpita2803@yahoo.com"
PASSWORD = "wpsinmktkghjpfkr"


class NotificationManager:

    # def __init__(self):
    #     self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        # message = self.client.messages.create(
        #     body=message,
        #     from_=TWILIO_VIRTUAL_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER,
        # )
        # # Prints if successfully sent.
        # print(message.sid)
        print(message)

    def send_emails(self, message, user_details, google_link):
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            for name, email in user_details:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\nDear {name},\n\n{message}\n{google_link}".encode('utf-8')
                )

