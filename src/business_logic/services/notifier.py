from notifypy import Notify


class NotifierService():
    def __init__(self, title, message) -> None:
        self.title = title
        self.message = message

    def display(self):
        notification = Notify()
        notification.title = self.title
        notification.message = self.message
        notification.send()
