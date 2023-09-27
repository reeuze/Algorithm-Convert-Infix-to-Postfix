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
            return int(var1)+int(var2)
        elif operator=='-':
            return int(var1)-int(var2)
        elif operator=='*':
            return int(var1)*int(var2)
        elif operator=='/':
            return int(var1)/int(var2)
        elif operator=='^':
            return int(var1)**int(var2)
    def Priority(self, input=[], index=0):
        self.Char = []
        self.Num = []
        # print(input, len(input))
        while input:
            # print(index, input[index])
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(input.pop(index))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            # print(self.Char, self.Num)
        i = 0
        best  = 0 
        while len(self.Num) != 1:
            for j, operator in enumerate(self.Char):
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
            # print(i)
            # print("var1 :", self.Num[i], "var2 :", self.Num[i+1], "oper :", self.Char[i])
            hasil = self.Operation(self.Num.pop(i), self.Num.pop(i), self.Char.pop(i))
            self.Num.append(hasil)
        return input[index-1]
    def Replace_operator(self, op1, op2):
        i = 0
        j = 0
        if op1=='+' or op1=='-':
            i = 1
        elif op1=='*' or op1=='/':
            i = 2
        elif op1=='^':
            i = 3
        elif op2=='+' or op2=='-':
            j = 1
        elif op2=='*' or op2=='/':
            j = 2
        elif op2=='^':
            j = 3
        print("i = ", i, "j = ", j)
        if i>=j:
            return op1
        elif i<j:
            return op2
    # def Forward_index(self, input=[], index=0):
    #     for i in range(index, len(input)):
    #         if input[i]==')':
    #             index += 1
    #     return index
    def Algorithm(self, input=[], index=0):
        for i in range(index, len(input)):
            print("i = ",  i)
            if input[i]=='(':
                self.Character.append(input[i])
                self.Print(input[i])
                input.append(self.Algorithm(input, i+1))
                # i += self.Forward_index(input, i+1)
                print("i diubah menjadi : ", i)
                # i += index
            elif input[i].isdigit():
                self.Postfix.append(input[i])
            elif self.Is_Operator(input[i]) is True:
                if self.Is_Operator(self.Character[-1]) is True:
                    self.Postfix.append(self.Replace_operator(self.Character.pop(), input[i]))
                else:
                    self.Character.append(input[i])
            elif input[i]==')':
                return self.Priority(input, index)
            elif input[i]==input[-1]:
                return self.Priority(input, index)
            self.Print(input[i])

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
# print(a.Input)
hasil = a.Algorithm(a.Input)
print("\nhasilnya : ", hasil)