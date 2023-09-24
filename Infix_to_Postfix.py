class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Number = []
        self.Stack = []
        self.Postfix = []
        self.Sum = 0
    def Print(self, input):
        print("scanned input : ", input)
        print("Stack :", ''.join(self.Stack))
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
    def Algorithm(self, input=[], index=0):
        if input[index].isDigit():
            self.Postfix.append(input[index])
            # self.Algorithm(input, index+1)
            sum = self.Operation(input[index], self.Algorithm(input, index+2), self.Algorithm(input, index+1))
            if sum is None:
                return input[index]
            else:
                return sum
        elif input[index]=='(':
            self.Stack.append(input[index])
            self.Algorithm(input, index+1)
        elif self.Is_Operator(input[index]) is True:
            
            self.Stack.append(input[index])
        elif input[index]==')':
            return input[index-1]
        elif input[index]==input[-1]:
            return input[index]
        self.Print(input[index])

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)