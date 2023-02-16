# Python-Try-Except

# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")    
# except:
#     print("Something else went wrong") 

# try:
#     print("Hello")   
# except:
#     print("Something went wrong")    
# else:
#     print("Nothing went wrong")    

#The finally block gets executed no matter if the try block raises any errors or not:
# try:
#     print(x)
# except:
#     print("Something went wrong")    
# finally:
#     print("The 'try except' is finished")    

#The try block will raise an error when trying to write to a read-only file:
# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing to the file")    
# finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  

# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = "hello"

# if no type(x) is int:
#     raise TypeError("Only integers are allowed")