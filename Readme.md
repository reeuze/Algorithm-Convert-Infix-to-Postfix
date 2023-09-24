Subject : Data structure and algorithm
Assesment #4

Create a program that will change from infix to postfix
This is the example of Infix convert to Postfix :

-- photo --

The algorithm :
1. Ubah input dari bentuk string menjadi stack input
2. Lakukan pemanggilan terhadap def Algorithm (self, input)
3. Apabila input merupakan digit
   a. append nilai input[index] ke stack Postfix
   b. Panggil func Algorithm 
4. Apabila input[index] adalah digit atau "("
   a. append 
5. Apabila input[index] adalah operator, maka lakukan operasi hitung dan return bentuk
postfix ke stack Temp setelah itu return hasil operasinya
6. Apabila input[index] adalah ")" atau input[-1]