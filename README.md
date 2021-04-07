# BinaryToDecimal-Converter
A converter binary number --> decimal number

***Hello !***

This program was a little project realised at school.
I had to make a converter which convert binary number (in the form of a list, for example : [1,0,1,0,0,1] ) to a decimal number.
I had to use Python to code this program.

The function has as parameter, the list which stores the binary value, named `l`

## How it works ?

```py 
def convert(l):
    intNumber = 0
    l.reverse()
    if len(l) == 0:
        return None
    for i in range(len(l)):
        if l[i] == 0:
            nbr = 0
        if l[i] == 1:
            nbr = 2**i
        intNumber += nbr
    return intNumber
```


First, we create the variable `intNumber`, which stores the value of the final decimal number.

To be able to convert, we need to reverse the elements of the list
