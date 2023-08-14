#OcP , principio de abiertom cerrado, crear una clase que permita agregar extensiones apartir d euna clase base pero se niegue a recibir
#modificaciones a la clase base

class Notificator: #clase BAse
    def __init__(self, user, message):
        self.user = user 
        self.nessage = message
        
    def notication(self):
        raise NotImplemented
    
class EmailNotificator(Notificator): #extension 1
    def Notification(self):
        print(f"send message for email to {self.user.email}")
        
class SmsNotificator(Notificator): #extension 2
    def Notification(self):
        print(f"send message for SMS to {self.user.email}")
        
class WSPNotificator(Notificator): #extension 3
    def Notification(self):
        print(f"send message for whastsapp to {self.user.email}")

