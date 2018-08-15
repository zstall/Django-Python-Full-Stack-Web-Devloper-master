
# This will result in a SyntaxError
# print("hello)

# This will result in a NameError
# lst = [1,2,3]
# print(mylst)
try:
    f=open('simple.txt', 'w')
    f.write("test write to simple Text!")
except:
    print("Error: could not find file or write data!")
else:
    print("Success!")
    f.close()


try:
    f=open('simple.txt', 'r')
    f.write("test write to simple Text!")
except:
    print("Error: could not find file or write data!")
else:
    print("Success!")
    f.close()

print("This does not kill your code")


try:
    f=open('simple.txt', 'r')
    f.write("test write to simple Text!")
except:
    print("Error: could not find file or write data!")
finally:
    print("I always work no matter what!")
    f.close()
