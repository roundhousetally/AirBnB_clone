# AirBnB Clone Interpreter :computer:

A python command interpreter written as part of the year one curriculum at Holberton School.

## Description :speech_balloon:

**AirBnB Clone Interpreter** is a python command interpreter that reads commands and manipulates data storge using json serialization.

## Invocation and Usage :computer:
**AirBnB Clone Interpreter** is invoked by calling

`./console.py`

Once launched it will display the prompt (hbnb).  From here **AirBnB Clone Interpreter** can be used like the command line within a narrow scope. **AirBnB Clone Interpreter** accepts the following commands:

### create
Creates a new instance of a model, saves it, and prints the id
Usage:
`(hbnb) create <model name>`

e.g.:

`(hbnb) create BaseModel`

### show
Searches the file for an instance that mataches the Model and id and displays its string represenation.
Usage:
`(hbnb) show <model name> <id>`

e.g.:

`(hbnb) show BaseModel 1143234253465`

### destroy
Searches the file for an instance that mataches the Model and id and deletes it.
Usage:
`(hbnb) destroy <model name> <id>`

e.g.:

`(hbnb) destroy BaseModel 1143234253465

### all
Prints all instances in storage file
Usage:

`(hbnb) all`

### update
Searches the storage file and updates a value at a particular instance
`update <class name> <id> <attribute name> "<attribute value>
"`

e.g.:

`update BaseModel 1143234253465 email "aibnb@holbertonschool.com"`

To exit:
`(hbnb) quit`


This will return the user to their home command line.

## authors :pencil2:
Jacob Ide Github: [ihavemadefire](https://github.com/ihavemadefire)

Tahlia Roper Github: [roundhousetally](https://github.com/roundhousetally)