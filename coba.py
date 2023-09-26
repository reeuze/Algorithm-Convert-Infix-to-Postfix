class Coba:
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

temp = ['*', '^']
number = ['4', '5', '6']
a = Coba()
hasil = a.Priority(temp, number)
print("Hasilnya = ", hasil)