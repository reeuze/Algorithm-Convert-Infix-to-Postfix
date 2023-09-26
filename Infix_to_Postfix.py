class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Temp = []
        self.Number = []
        self.Character = []
        self.Postfix = []
    def Print(self, input):
        print("scanned input : ", input)
        print("Stack :", ''.join(self.Character))
        print("Postfix :", ''.join(self.Postfix), "\n")
    def Convert(self, input):
        self.Input.append('(')
        for char in input:
            self.Input.append(char)
        self.Input.append(')')
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Operation(self, var1, var2, operator):
        if operator=='+':
            return var1+var2
        elif operator=='-':
            return var1-var2
        elif operator=='*':
            return var1*var2
        elif operator=='/':
            return var1/var2
        elif operator=='^':
            return var1^var2
        return None
    def Priority(self, index):
        operators = [['+', '-'], ['*', '/'], ['^']]
        for i, operator in range(index, len(self.Temp)):
            for j in range(0, 2):
                if operator==operators(3):
                    self.Number[i] = self.Operation(self.Number.pop[i], self.Number.pop[i+1], self.Temp.pop[i])
                elif operator==operators(2):
                    self.Number[i] = self.Operation(self.Number.pop[i], self.Number.pop[i+1], self.Temp.pop[i])
                elif operator==operators(2):
                    self.Number[i] = self.Operation(self.Number.pop[i], self.Number.pop[i+1], self.Temp.pop[i])
        return
    def Algorithm(self, input=[], index=0):
        digit = 0
        digit_in = 0
        for i in range(index, len(input)):
            if input[index]=='(':
                self.Character.append(input[i])
                self.Print(input[i])
                self.Algorithm(input, i+1)
                digit += 1
            # disini bagian perhitunganya
            elif input[index].isdigit():
                self.Number.append(input[index])
                self.Postfix.append(input[index])
                self.Print(input[index])
                digit += 1
                digit_in += 1
            elif self.Is_Operator(input[index]) is True:
                self.Temp.append(input[index])
                self.Character.append(input[index])
            elif input[index]==')':
                self.Priority(digit-digit_in-1)
                return
            elif input[index]==input[-1]:
                self.Priority(digit-digit_in-1)
                return
            
        self.Print(input[index])

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
a.Algorithm(a.Input)
print(''.join(a.Number))