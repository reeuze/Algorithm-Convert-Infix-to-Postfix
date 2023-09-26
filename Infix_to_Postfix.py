class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Number = []
        self.Character = []
        self.Temp = []
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
    def Priority(self, temp=[]):
        for i in range(len(temp)):
            for j, operator in enumerate(temp):
                if operator=='^':
                    
            if self.Temp[i]=='^':
                sum = self.Operation(self.Number.pop(i), self.Number.pop(i+1), self.Temp.pop(i))
            elif self.Temp[i]=='*' or self.Temp[i]=='/':
                sum = self.Operation(self.Number.pop(i), self.Number.pop(i+1), self.Temp.pop(i))
            elif self.Temp[i]=='+' or self.Temp[i]=='-':
                sum = self.Operation(self.Number.pop(i), self.Number.pop(i+1), self.Temp.pop(i))
            self.Number[i-1] = sum
        return
    def Algorithm(self, input=[], index=0):
        digit = 0
        digit_in = 0
        temp = []
        for i in range(index, len(input)):
            if input[i]=='(':
                self.Character.append(input[i])
                self.Algorithm(input, i+1)
                digit += 1
            elif input[i].isdigit():
                self.Number.append(input[i])
                self.Postfix.append(input[i])
                digit += 1
                digit_in += 1
            elif self.Is_Operator(input[i]) is True:
                temp.append(input[i])
                self.Character.append(input[i])
            elif input[i]==')':
                self.Priority(temp)
                return
            elif input[i]==input[-1]:
                self.Priority(temp)
                return
            self.Print(input[i])

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
a.Algorithm(a.Input)
print(''.join(a.Number))