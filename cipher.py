class cipher:
    def __init__(self, message, location):
        self.message=message #Original message
        self.location=location #Location to which the message is to be sent
        self.translation='' #Variable which stores the translation into the cipher
        self.alpha='abcdefghijklmnopqrstuvwxyz' #Just used to simplify code later on
        for x in range(len(self.message)):
            if self.message[x].isalpha(): #Translate characters one by one, then adds them to final "translated" variable
                self.char=self.alpha[(self.alpha.find(self.message[x].lower())+3)%26] #Shift characters three spots forwards in the alphabet
            else:
                self.char=self.message[x] #Don't shift characters if they're not letters
            if self.message[x].lower()!=self.message[x]:
                self.char=self.char.upper()
            self.translation=self.translation+self.char #Appends characters to string