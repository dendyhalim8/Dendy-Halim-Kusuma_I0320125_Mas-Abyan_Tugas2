a = 4        # 4  = 0000 0100
b = 11       # 11 = 0000 1011

c = a | b;  # 15 = 0000 1111
print ("Line 1 - Value of c is ", c)

c = a >> b;  # 0 = 0000 0000
print ("Line 2 - Value of c is", c)

c = a^ b;   # 15 = 0000 1111
print ("Line 3 - Value of c is ", c)

c = ~a;   # -5 = - 0000 0101
print ("Line 4 - Value of c is ", c)

c = a & b;   # 0 = 0000 0000
print ("Line 5 - Value of c is ", c)