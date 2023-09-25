Subject : Data structure and algorithm
Assesment #4

Create a program that will change from infix to postfix
This is the example of Infix convert to Postfix :

-- photo --

The algorithm :
1. Ubah input dari bentuk string menjadi stack input
2. Lakukan pemanggilan terhadap func Algorithm
3. Apabila input merupakan digit
   a. append nilai input[index] ke stack Postfix
4. Apabila input[index] adalah digit atau "("
   a. append nilai input
   b. Panggil func Algorithm
5. Apabila input[index] adalah operator
   a. Check 5 langkah 
   a. Check prioritas menggunakan func Priority
      i. Apabila prioritasnya lebih kecil
6. Apabila input[index] adalah ")" atau input[-1]