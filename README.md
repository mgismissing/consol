# Consol
Do you know what Python is?  
And can you use Python to replace assembly code? Probably not.  
This repository will make it possible.

## Download
Before you do anything you will need to download this repository.
Note that for now it will only work for Windows computers, but once I finish fixing bugs I will make it available on other operative systems too.  
You only need to clone this repository. Type ```git clone https://github.com/mgismissing/consol```.

## Projects
### Creating a project
To create a project, type in the same directory as the ```consol.bat``` file ```consol make <name>``` where name is the project's name. The project will be created in the same directory.
### Deleting a project
To delete a project, type in the same directory as the ```consol.bat``` file ```consol del <name>``` where name is the project's name. Note that Consol will only detect and delete projects that are in the same directory as the ```consol.bat``` file.

## Customizing the translator
### Changing the instructions
Not every assembly language is the same. To customize the translator edit ```dictionary.py```. You will find something similar to this:
``` python
convert_dict = {
    "add": "ADDabc"
    "divide" : "DIVabc"
}
```
The keys (the first values) are the python functions, and the values (the strings after the keys) are the corresponding assembly instruction. Edit the values to change the output assembly file. For example if ```dictionary.py``` is like the one above and I write the code
``` python
add(1, 1, 0)
```
The output will be the following:
```
ADD110
```
This below is another example of ```dictionary.py```, the code and its output.
``` python
convert_dict = {
    "add": "SUM[a+b+c]"
    "divide": "DIV[a+b+c]"
}
```
``` python
add(1, 1, 0)
```
```
SUM[1+1+0]
```
Another example with less arguments and changed argument order:
``` python
convert_dict = {
    "add": "ADD b_a"
    "divide": "DIV b_a"
}
```
``` python
add(1, 0)
```
```
ADD 0_1
```
### Adding/Removing an instruction
Sadly this functionality is not ready yet.
## Editing the code
Edit the code you find in ```<your_project_name>.cnc```.

## Converting the code
In the same directory as ```consol.bat``` type ```consol```. You will be asked for the project filename. Type it and press enter. You will find the converted file in this directory as ```<your_project_filename>.asm```. Example:  
If the code file is ```my_code.cnc``` the assembly file will be ```my_code.cnc.asm```.