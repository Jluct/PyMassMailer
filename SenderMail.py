import time
from smtplib import SMTPDataError


class SenderMail:
    sender = ''
    address = ''
    conf = []

    def __init__(self, conf, sender):
        self.conf = conf
        self.sender = sender.SMTP(
            self.conf.get('smtp', 'host'),
            self.conf.get('smtp', 'port')
        )

        if self.conf.get('smtp', 'login') and self.conf.get('smtp', 'password'):
            self.sender.login(
                self.conf.get('smtp', 'login'),
                self.conf.get('smtp', 'password')
            )

    def __del__(self):
        self.sender.quit()

    def set_address(self, address):
        self.address = address
        return self

    def send_all(self, subject='Re:', delay=True):
        for item in self.address:
            self.send_one(item, subject, delay)

    def send_one(self, email, subject='Re:', delay=True):
        try:
            self.sender.sendmail(
                self.conf.get('smtp', 'from'),
                [email],
                "\r\n".join((
                    "From: %s" % self.conf.get('smtp', 'from'),
                    "To: %s" % email,
                    "Subject: %s" % subject,
                    "",
                    "Python test PyMassMailer"
                ))
            )

            if self.conf.get('smtp', 'delay') and delay:
                time.sleep(int(self.conf.get('smtp', 'delay')) / 1000)

        except SystemError:
            print("Mail not send")
        except SMTPDataError:
            print('SPAM DETECTED')

        return True
