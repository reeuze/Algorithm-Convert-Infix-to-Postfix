class Infix_Postfix:
    def __init__(self):
        self.Input = []
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
    def Convert (self, input):
        for char in input:
            self.Input.append(char)
    def Algorithm(self, input=[], index=0):
        if input[index].isDigit() or input[index]=='(':
            self.Algorithm(input, index+1)
        

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)