Subject : Data structure and algorithm
Assesment #4

Create a program that will change from infix to postfix
This is the example of Infix convert to Postfix :

-- photo --

The algorithm :
1. Ubah input dari bentuk string menjadi stack input
2. Lakukan pemanggilan terhadap def Algorithm (self, input)
3. Cek apakah input merupakan digit atau tidak
4. Apabila input[index] adalah digit atau "(", maka panggil def Algorithm (self, input)
5. Apabila input[index] adalah operator, maka lakukan operasi hitung dan return bentuk
postfix ke stack Temp setelah itu return hasil operasinya
6. Apabila input[index] adalah ")" atau input[-1]