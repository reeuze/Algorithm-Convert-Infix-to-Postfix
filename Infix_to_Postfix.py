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
                break
            else:
                postfix.append(character.pop())
            i -= 1
    def calculation(self, input=[], index=0):
        self.Char = []
        self.Num = []
        # print(input, index)
        while input:
            # print(index, input[index])
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(str(input.pop(index)))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            else:
                self.Num.append(str(input.pop(index)))
            # print(self.Char, self.Num)
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
                # print(best)
                # time.sleep(2)
            # print(n)
            # print("var1 :", self.Num[i], "var2 :", self.Num[i+1], "oper :", self.Char[i])
            # print(self.Num)
            hasil = self.Operation(self.Num[i], self.Num[i+1], self.Char.pop(i))
            self.Num.insert(i, str(hasil))
            self.Num.pop(i+1)
            self.Num.pop(i+1)
            # print(self.Num, len(self.Num))
            if len(self.Num) == 1:
                break
            # time.sleep(2)
        # print(self.Num)
        input[index] = self.Num.pop()
        input[index-1] =  str(input.pop(index))
        # print(input)
        # time.sleep(4)
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
        # print("i = ", i, "j = ", j)
        if i>=j:
            return op1
        elif i<j:
            return op2
    # def Forward_index(self, input=[], index=0):
    #     for i in range(index, len(input)):
    #         if input[i]==')':
    #             index += 1
    #     return index
    def fixing_stack(self, input=[]):
        for i in range(len(input)):
            if input[i] is not None:
                input[i].append()
    def Algorithm(self, input=[], index=0):
        for i in range(index, len(input)):
            # print("i = ",  i)
            # print("elemen : ", input[i])
            if len(input) == 1:
                break
            elif input[i]=='(':
                self.Character.append(input[i])
                self.Print(input[i])
                self.Algorithm(input, i+1)
                # i += self.Forward_index(input, i+1)
                # i += index
            elif input[i].isdigit():
                self.Postfix.append(input[i])
            elif self.Is_Operator(input[i]) is True:
                if self.Is_Operator(self.Character[-1]) is True:
                    self.Postfix.append(self.Replace_operator(self.Character.pop(), input[i]))
                else:
                    self.Character.append(input[i])
            elif input[i]==')':
                # self.fixing_stack(input)
                self.Fix_character(self.Character, self.Postfix)
                self.calculation(input, index)
                return
            self.Print(input[i])
            time.sleep(1)

input = "1+(2/3-(4*5^6)+7)*8"
a = Infix_Postfix()
a.Convert(input)
# print(a.Input)
hasil = int(a.Input)
print("\nHasilnya : ", hasil)