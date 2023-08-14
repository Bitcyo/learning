from abc import ABC, abstractmethod

class VerifySpeling(ABC):
    def VerifyWords(self):
        pass
    
    
class Dictionario(VerifySpeling):
    def VerifyWords(self, word):
        pass
    
class CorrectlySpeling(ABC):
    def __init__(self, verify):
        self.verify = verify
        
    def correct_text():
        pass