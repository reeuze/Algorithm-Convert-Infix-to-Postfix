class Coba:
    def __init__(self):
        self.Input = []
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
    def Priority(self, input=[], index=0):
        self.Char = []
        self.Num = []
        print(input, len(input))
        while input:
            print(index, input[index])
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(input.pop(index))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            print(self.Char, self.Num)
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
            print(i)
            print("var1 :", self.Num[i], "var2 :", self.Num[i+1], "oper :", self.Char[i])
            hasil = self.Operation(self.Num.pop(i), self.Num.pop(i), self.Char.pop(i))
            self.Num.append(hasil)
        input[index] = self.Num.pop()
        print(input)

input = "1+2*3^4)+7"
a = Coba()
a.Convert(input)
a.Priority(a.Input)