class Student:
    def __init__(self):
        pass 
        
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        
    def raise_hand(self):
        print("Pick me!")
    
class ChattyStudent(Student):
    def __init__(self):
        super().__init__()
    
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
        
    def raise_hand(self):
        super().raise_hand() 
        for _ in range(9):
            print ("Pick me!")
    
    # #Why not 
    #     time = super().raise_hand()
    #     return time *10