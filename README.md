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
To be able to convert, we need to reverse the elements of the list.
We check the state of the list : we return None if the list is empty

Now, for each elements in the list, if the element is 1, we do 2 power i : ` nbr = 0`.
Else if the element is 0, so `nbr = 0`.

When the for loop is finished, we return `intNumber`

## ***Examples***

```py
print(convert([1,0,1,0,0,1,1]))
print(convert([1,0,1,0]))
``` 
* If we execute the first line, the function will return `83`  
______________  
        1   0   1   0   0   1   1

#### *we reverse :* 
        1   1   0   0   1   0   1  
        
     2^0 + 2^1 + 0 + 0 + 2^4 + 0 + 2^6
     ==> 83


* If we execute the second line, the function will return `10`
______________  
        1   0   1   0

#### *we reverse :* 
        0   1   0   1  
    
       0 + 2^1 + 0 + 2^3
       ==> 10


## Thanks you for reading

If you have questions, say me !

### *BYE ! !*
