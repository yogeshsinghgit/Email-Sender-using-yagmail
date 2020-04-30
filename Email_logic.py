import yagmail  # pip install yagmail
from plyer import notification
class LogicMail():
    def __init__(self,sender_email,sender_password):

        self.sender_email = sender_email
        self.sender_password = sender_password

    def send(self,receiver_email,subject,text_message,attachment):
        self.receiver = receiver_email
        self.subject = subject
        self.message = text_message
        self.receiver = self.receiver.split(',')
        self.attach = attachment

        if len(self.attach) == 0:
            yag = yagmail.SMTP(user=self.sender_email, password=self.sender_password)
            yag.send(self.receiver, self.subject, self.message)
            notification.notify(title="Sender Says",message=" Mail is sent",timeout=5)
        else:
            yag = yagmail.SMTP(user=self.sender_email, password=self.sender_password)
            yag.send(self.receiver, self.subject, self.message,self.attach)
            notification.notify(title="Sender Says", message=" Mail is sent", timeout=5)


