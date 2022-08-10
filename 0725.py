#method vs function
# we ccall method using s.f() rather than f(s):

s = "hello world"
print(len(s)) #len is a function
print(s.upper()) #upper is a string method, called using the . notation
print(s.replace("hello", "bye"))

#ex)    n = 123
#       print(len(n))      -> type error - len is a function for the str type
#       print(n.upper())   ->   attribute error - this means there is no method upper() for int 
