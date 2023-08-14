import smtplib
import imaplib


class EmailFacad:
    def __init__(self, host, user_name, password):
        self.host = host
        self.user_name = user_name
        self.password = password

    def send_email(self, to_email, subject, msg):
        if not "@" in self.user_name:
            from_email = f"{self.user_name}@{self.host}"
        else:
            from_email = self.user_name

        message = f'"From":{from_email} \
                "To":{to_email}   \
                "Subject":{subject} \
                {msg} \
                '
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.user_name, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        pass


if __name__ == "__main__":
    host = "some_hostname"
    user_name = "user_name"
    password = "password"
    email = EmailFacad(host, user_name, password)
    email.send_email(
        to_email="friend_email_address",
        subject="test_mail",
        msg="Hi Buddy, This is test mail",
    )
