import time
import quopri
from smtplib import SMTPDataError


class SenderMail:
    templating = ''
    sender = ''
    address = ''
    conf = []

    def __init__(self, conf, sender, templating):
        self.templating = templating
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

    def send_all(self, tpl, data='', subject='Re:', delay=True):
        for item in self.address:
            self.send_one(item, tpl, data, subject, delay)

    def send_one(self, email, tpl, data='', subject='Re:', delay=True):
        try:
            template = quopri.encodestring(self.templating.render(tpl, data).encode())
            print(template)

            self.sender.sendmail(
                self.conf.get('smtp', 'addr'),
                [email],
                "\r\n".join((
                    "From: %s" % self._merge_sender_addr(),
                    "To: %s" % email,
                    "Subject: %s" % subject,
                    "MIME-Version: 1.0",
                    "Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: quoted-printable",
                    "",
                    template.decode('utf-8')
                ))
            )

            if self.conf.get('smtp', 'delay') and delay:
                time.sleep(int(self.conf.get('smtp', 'delay')) / 1000)

        except SystemError:
            print("Mail not send")
        except SMTPDataError:
            print('SPAM DETECTED')
        else:
            return True

    def _merge_sender_addr(self):
        if self.conf.get('smtp', 'from'):
            return self.conf.get('smtp', 'from') + " <" + self.conf.get('smtp', 'addr') + ">"
        else:
            return self.conf.get('smtp', 'addr')
