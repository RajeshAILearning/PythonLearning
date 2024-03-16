try:
    #open random file fail try to catch that error
    with open('filelog.txt','r') as reader:
        reader.read()
except:
    print("I reached here because there is a failure in try block")

try:
    #open actual existing file so catch wont executed here
    with open('test.txt','r') as reader:
        reader.read()
except:
    print("I reached here because there is a failure in try block")

#TO capture Pythons Error Message use - except Exception as e
try:
    #open random file fail try to catch that error
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

#Finally - connected with try and except, this block will be executed always
try:
    #open random file fail try to catch that error
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources - not existing file")

try:
    #open actual existing file so catch wont executed here
    with open('test.txt','r') as reader:
        reader.read()
except:
    print("I reached here because there is a failure in try block")

finally:
    print("Cleaning up")

#Finally- example you are doing some creation and after execution you dont want to keep those records so you can
#delete those using finally block, even you got stuck while creating want to delete the junk, use fianlly
