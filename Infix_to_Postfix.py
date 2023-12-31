import time
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
            return float(var1)+float(var2)
        elif operator=='-':
            return float(var1)-float(var2)
        elif operator=='*':
            return float(var1)*float(var2)
        elif operator=='/':
            return float(var1)/float(var2)
        elif operator=='^':
            return float(var1)**float(var2)
    def Fix_character(self, character=[], postfix=[]):
        i = len(character) - 1
        while i >= 0:
            if character[i]=='(':
                character.pop()
                break
            else:
                postfix.append(character.pop())
            i -= 1
    def calculation(self, input=[], index=0):
        self.Char = []
        self.Num = []
        while input:
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(str(input.pop(index)))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            else:
                self.Num.append(str(input.pop(index)))
        while True:
            i = 0
            best  = 0
            for j, operator in enumerate(self.Char):
                if (operator=='+' or operator=='-') and best < 1:
                    n = 1
                    i = j
                elif (operator=='*' or operator=='/') and best < 2:
                    n = 2
                    i = j
                elif operator=='^' and best < 3:
                    n = 3
                    i = j
                best = n
            hasil = self.Operation(self.Num[i], self.Num[i+1], self.Char.pop(i))
            self.Num.insert(i, str(hasil))
            self.Num.pop(i+1)
            self.Num.pop(i+1)
            if len(self.Num) == 1:
                break
        input[index] = self.Num.pop()
        input[index-1] =  input.pop(index)
    def Replace_operator(self, op1, op2):
        i = 0
        j = 0
        if op1=='+' or op1=='-':
            i = 1
        elif op1=='*' or op1=='/':
            i = 2
        elif op1=='^':
            i = 3
        if op2=='+' or op2=='-':
            j = 1
        elif op2=='*' or op2=='/':
            j = 2
        elif op2=='^':
            j = 3
        if i>=j:     # stack more important
            self.Postfix.append(op1)
            self.Character.pop()
            self.Character.append(op2)
        elif i<j:   # input more important
            self.Character.append(op2)
    def Algorithm(self, input=[], index=0):
        for i in range(index, len(input)):
            if len(input) == 1:
                break
            elif input[i]=='(':
                self.Character.append(input[i])
                self.Print(input[i])
                self.Algorithm(input, i+1)
            elif input[i].isdigit():
                self.Postfix.append(input[i])
            elif self.Is_Operator(input[i]) is True:
                if self.Is_Operator(self.Character[-1]) is True:
                    self.Replace_operator(self.Character[-1], input[i])
                else:
                    self.Character.append(input[i])
            elif input[i]==')':
                self.Fix_character(self.Character, self.Postfix)
                self.calculation(input, index)
                return
            self.Print(input[i])
            time.sleep(1.5)
        return ''.join(self.Input)

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
hasil = a.Algorithm(a.Input)
print("\nHasilnya : ", hasil)