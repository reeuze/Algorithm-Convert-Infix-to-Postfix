class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Character = []
        self.Postfix = []
    def Print(self, input):
        print("scanned input : ", input)
        print("Stack :", ''.join(self.Character))
        print("Postfix :", ''.join(self.Postfix))
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
    def Priority(self, Temp=[], Number=[]):
        while len(Number) != 1:
            best = 0
            i = 0
            for j, operator in enumerate(Temp):
                if operator=='+' or operator=='-' and best < 1:
                    n = 1
                    i = j
                elif operator=='*' or operator=='/' and best < 2:
                    n = 2
                    i = j
                elif operator=='^' and best < 3:
                    n = 3
                    i = j
                best = n
            print("var1 :", Number[i], "var2 :", Number[i+1], "oper :", Temp[i])
            hasil = self.Operation(Number.pop(i), Number.pop(i), Temp.pop(i))
            Number.append(hasil)
        return Number.pop()
    # def Forward_index(self, input=[], index=0):
    #     for i in range(index, len(input)):
    #         if input[i]==')':
    #             index += 1
    #     return index
    def Algorithm(self, input=[], Temp=[], Number=[], i=0):
        Number = []
        Temp = []
        h = len(input)
        while i <= h:
            if input[i]=='(':
                self.Character.append(input[i])
                self.Print(input[i])
                hasil = self.Algorithm(input, Temp, Number, i)
                # index += self.Forward_index(input, i+1)
                Number.append(hasil)
                # i += index
            elif input[i].isdigit():
                Number.append(input[i])
                self.Postfix.append(input[i])
            elif self.Is_Operator(input[i]) is True:
                Temp.append(input[i])
                self.Character.append(input[i])
            elif input[i]==')':
                return self.Priority(Temp, Number)
            elif input[i]==input[-1]:
                return self.Priority(Temp, Number)
            self.Print(input[i])
            print(Temp, Number, "\n")
            i += 1

input = "1+(2/3-(4*5^6)+7)*8"
Temp = []
Number = []
a = Infix_Postfix()
a.Convert(input)
hasil = a.Algorithm(a.Input, Temp, Number)
print("\nhasilnya : ", hasil)