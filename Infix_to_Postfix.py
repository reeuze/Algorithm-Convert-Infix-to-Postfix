class Infix_Postfix:
    def __init__(self):
        self.Input = []
        self.Number = []
        self.Stack = []
        self.Postfix = []
        self.Operator = '+'
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
    def Priority(self, operator1, operator2):
        operators = [['+', '-'], ['*', '/'], ['^']]
        if operator1.index(operators) > operator2.index(operators):
            return operator1
        elif operator1.index(operators) < operator2.index(operators):
            return operator2
        elif operator1.index(operators) == operator2.index(operators):
            return operator1
    def Algorithm(self, input=[], index=0):
        if input[index].isdigit():
            self.Postfix.append(input[index])
            self.Print(input[index])
            self.Algorithm(input, index+1)
        elif input[index]=='(':
            self.Stack.append(input[index])
            self.Print(input[index])
            self.Algorithm(input, index+1)
        elif self.Is_Operator(input[index]) is True:
            self.Priority(input[index], self.Stack.peek())
            self.Stack.append(input[index])
        elif input[index]==')':
            return input[index-1]
        elif input[index]==input[-1]:
            return input[index]
        self.Print(input[index])

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
a.Algorithm(a.Input)