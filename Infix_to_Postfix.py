class Infix_Postfix:
    def __init__(self):
        self.Number = []
        self.Character = []
        self.Temp = []
        self.Postfix = []
        self.Sum = 0
    def Summation(self, a, b):
        return a+b
    def Subtraction(self, a, b):
        return a-b
    def Multiplication(self, a, b):
        return a*b
    def Distribution(self, a, b):
        return a/b
    def Rank(self, a, b):
        return a^b
    def Priority(self, var):
        if var==')':
            return var
        elif var=='(':
            print("A")
    def Convert(self, String):
        for char in String:
            if char.isdigit():
                self.Number.append(char)
            else:
                self.Temp.append(char)

    # def Postfix(self, var):

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()