'''
# Unit Testing
- pylint : this is lib that looks at your code and reports back possible issues
- unittest: this built-in library will allow to test your own programs and check you are getting desired outputs
'''

A=1
B=3
print(a+B) #run using pylint notebook6.py

'''
The following is the output: 
************* Module notebook6
notebook6.py:4:0: C0301: Line too long (112/100) (line-too-long)
notebook6.py:11:0: C0304: Final newline missing (missing-final-newline)
notebook6.py:7:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
notebook6.py:8:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
notebook6.py:9:8: E0602: Undefined variable 'B' (undefined-variable) -> E idetitfies as Error 
-----------------------------------
Your code has been rated at 0.00/10
'''
