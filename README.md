# Consol
Do you know what Python is?  
And can you use Python to replace assembly code? Probably not.  
This repository will make it possible.

## Download
Before you do anything you will need to download this repository.
Note that for now it will only work for Windows computers, but once I finish fixing bugs I will make it available on other operative systems too.  
Start by running  ```git clone https://github.com/mgismissing/consol```. Then in the same directory type ```consol install```. With this command consol will install all of the required dependencies. Don't worry, if you already installed one of those it will simply update them to the latest version.

## Projects
### Creating a project
To create a project, type in the same directory as the ```consol.bat``` file ```consol make <name>``` where name is the project's name. The project will be created in the same directory.
### Deleting a project
To delete a project, type in the same directory as the ```consol.bat``` file ```consol del <name>``` where name is the project's name. Note that Consol will only detect and delete projects that are in the same directory as the ```consol.bat``` file.
### Updating a project
Outdated, will be removed later. This functionality is no longer needed.

## Other commands
### Clear the cache
When Consol runs a ```.cnc``` file it will create a temporary file in the ```open``` folder. To remove all of the files in the ```open``` folder simply type ```consol clear```.

## Customizing the translator
Not every assembly language is the same. Will it be the opcodes or how memory is handled. To customize the translator file go in the ```convert``` folder and edit ```dict.py```. You will find something similar to this:
``` python
convert_dict = {
    "add": "ADDabc"
    "divide" : "DIVabc"
}
```
The keys (the first values) are the python functions, and the values (the strings after the keys) are the corresponding assembly opcode. Edit the values to change the output assembly file. For example if ```dict.py``` is like the one above and I write the code
``` python
add(1, 1, 0)
```
The output will be the following:
```
ADD110
```
This below is another example of ```dict.py```, the code and its output.
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
## Editing the code
Edit the code you find in ```<your_project_name>.cnc```.

## Converting the code
In the same directory as ```consol.bat``` type ```consol <your_project_filename>```.