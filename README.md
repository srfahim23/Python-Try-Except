# Python-Try-Except
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
When an error occurs,  or exception as we call it, Python will normally stop and generae an error message.

These exceptions can be handled using the try statement:

Example:

The try block will generate an exception, because x is not defined:

    try:
        print(x)
    except:
        print("An exception occured")    

Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an erro:

Example:

This statement will raise an error, because x is not defined:

    #This will raise an exception, because x is not defined:

    print(x)

# Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example:

Print one message if the try block raises a NameError and another for other errors:

    #The try block will generate a NameError, because x is not defined:

    try:
        print(x)
    except NameError:
        print("Varaible x is not defined")
    except:
        print("Something else went wrong")    
