class dad:
    def __init__(self,eyes,aggressive):
        self.eyes=eyes
        self.aggressive=aggressive
    def display(self):
        print("Your eye colour is ",self.eyes)
        print("You are aggressive",self.aggressive)
class son(dad):
    def __init__(self,name,age,eyes,aggressive):
        self.name=name
        self.age=age
        # dad.__init__(self,eyes,aggressive)
        super(). __init__(var1,var2)
obj=son("Ishaan",11,"Black",False)  
obj.display()      
