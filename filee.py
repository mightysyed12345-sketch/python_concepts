#file I/O:.text and binary files
#what are text files:
# Text files are files that contain human-readable characters, typically stored in a format that can be edited with a simple text editor.
#what are binary files:
# Binary files are files that contain data in a format that is not directly readable by humans, typically stored in a format that requires a specific program to interpret and display.
#give me all the modes of text files with codes examples:
f=open("sample.txt","r+")#r+ used to add text at the initial position and w+ write text at the initial position and a+ used to add text at the end of the file
#w+ used to delete the existing text and write new text at the initial position
data=f.write("iam here to learn python in a advanced way")
f.seek(0)  # Move the file pointer to the beginning to getting read it 
datay=f.read()
print(data)
print(datay)
f.close()
#we use with open as f:to avoid closing the file manually 
with open("sample.txt","r+") as f:
    data=f.write("iam getting placed in google")
    f.seek(0)
    print(data)
    datay=f.read()
    print(datay)
#word search code in text files:
with open("sample.txt","r") as f:
    content=f.read()
    word="python"
    if word in content:
        print(f"The word '{word}' is found in the file.")
    else:
        print(f"The word '{word}' is not found in the file.")

#please give me the code for exception handling try,except,finally in file I/O:
# Exception handling in file I/O using try, except, and finally
try:
    with open("sample.txt", "r") as f:
        content = f.read()
        word = "pythopn"
        if word in content:
            print(f"The word '{word}' is found in the file.")
        else:
            print(f"The word '{word}' is not found in the file.")
except FileNotFoundError:
    print("file sample.txt not found. Please check the file path and try again.")
except Exception as e:
    print(f"An error Occurred while reading the file: {e}")
finally:
    print("file operation is completed successfully.")

#list comprehension in file I/O:
# List comprehension can be used to read lines from a file and process them in a concise way
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]
    print(lines)
squarea=[]
for i in range(1,11):
    squarea.append(i**3)
print(squarea)

#json module in file I/O:
import json
# Writing JSON data to a file
#json.loads() is used to convert a JSON string into a Python object, while json.dumps() is used to convert a Python object into a JSON string.
#json.dump() is used to write a Python object as JSON data to a file, while json.load() is used to read JSON data from a file and convert it into a Python object.
#give me the examples of json.dump() and json.load():
# Example of json.dump() and json.load()
import json
json_str='{"name":"syedmohammed","isteacher":"yes it is mohammed","istrue":"true"}'
py_obj=json.loads(json_str)
print(type(py_obj),py_obj)
obbj=  {
    "name":"syedmohammed",
    "isTeacher":True,
    "roll number":"160125736058"
}
datau=json.dumps(obbj)
print(type(datau),datau)

import json
d={
    "name":"syed rehan",
    "age":67,
    "kaam":"loha"
}
with open("data.json","w") as f:#converting the json into python using file
    datai=json.dump(d,f)
    print(datai)

with open("data.json","r") as f:#converting the python into the json using the file
    py_obj=json.load(f)
    print(py_obj)