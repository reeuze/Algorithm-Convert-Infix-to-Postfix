Subject : Data structure and algorithm
Assesment #4

Create a program that will change from infix to postfix
This is the example of Infix convert to Postfix :

![alt text](https://github.com/reeuze/Algorithm-Convert-Infix-to-Postfix/blob/main/Image/Image%20Infix%20to%20Postfix.png?raw=true)

The algorithm :
1. Change the form of input which is still in string form to stack form, at the beginning and end with open and close brackets
2. Then check the elements one by one, using looping
3. If the element is an open bracket, then add the value to the character stack. Then do it recursively
4. If the element is a number, then add the value to the postfix stack
5. If the element has the operator value +/-/:/*/^, then add the value to the postfix operator, with the priority conditions below
   previous operator. If the operator has priority below the previous operator, then enter the previous value to the postfix stack,
   and add the operator to the character stack
6. If the element has the value of the closing bracket, then enter the operator in the character stack up to the opening bracket,
   then perform the operation count against the numbers in brackets