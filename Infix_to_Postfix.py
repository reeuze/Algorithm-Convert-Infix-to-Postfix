class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Character = []
        self.Postfix = []
    def Print(self, input):
        print("scanned input : ", input)
        print("Stack :", ''.join(self.Character))
        print("Postfix :", ''.join(self.Postfix), "\n")
    def Convert(self, input):
        for char in input:
            self.Input.append(char)
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Operation(self, var1, var2, operator):
        if operator=='+':
            return int(var1)+int(var2)
        elif operator=='-':
            return int(var1)-int(var2)
        elif operator=='*':
            return int(var1)*int(var2)
        elif operator=='/':
            return int(var1)/int(var2)
        elif operator=='^':
            return int(var1)**int(var2)
        return None
    def Priority(self, Temp=[], Number=[]):
        while not Temp:
            best = 0
            i = 0
            for j, operator in enumerate(Temp):
                if operator=='+' or operator=='-' and best < 1:
                    n = 1
                    i = j
                elif operator=='*' or operator=='/' and best < 1:
                    n = 2
                    i = j
                elif operator=='^' and best < 1:
                    n = 3
                    i = j
                best = n
            print("var1 : ", Number[i], "var2 : ", Number[i+1], "oper : ", Temp[i])
            self.Operation(Number.pop(i), Number.pop(i+1), Temp.pop(i))
        return Number.pop()
    def Algorithm(self, input=[], index=0):
        self.Temp = []
        self.Number = []
        for i in range(index, len(input)):
            if input[i]=='(':
                self.Character.append(input[i])
                self.Number[i] = self.Algorithm(input, i+1)
            elif input[i].isdigit():
                self.Number.append(input[i])
                self.Postfix.append(input[i])
            elif self.Is_Operator(input[i]) is True:
                self.Temp.append(input[i])
                self.Character.append(input[i])
            elif input[i]==')':
                return self.Priority(self.Temp, self.Number)
            elif input[i]==input[-1]:
                return self.Priority(self.Temp, self.Number)
            self.Print(input[i])
            print(self.Temp, self.Number)

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
# a.Algorithm(a.Input)
print("\nhasilnya : ", a.Algorithm(a.Input))