# AirBnB clone - The console
![hbnb](https://user-images.githubusercontent.com/107734098/223599965-315a2824-f81f-42fa-b981-3c9a1f333549.png)

This project is a command-line interface (CLI) application that allows users to manage objects in a database. Users can create, update, delete, and search for objects, as well as perform some advanced operations such as statistics.

## Command Interpreter

The command interpreter is the core of the application. It is responsible for accepting and parsing user input, and executing the corresponding actions.

## How to Start It
To start the command interpreter, run the following command in your terminal:

```$ ./console.py```




## How to Use It
Once the command interpreter is running, you can enter commands to manage objects in the database. The basic syntax for a command is:

```<command> <class> <id> <attributes>```

Where:

- ```<command>``` is one of the supported commands (create, show, destroy, all, update).
- ```<class> ```is the name of the class of objects you want to manage.
- ```<id>``` is the ID of the object you want to manage (not required for create and all commands).
- ```<attributes>``` are the attributes you want to create or update in the object (not required for create, show, destroy, and all commands).

To get a full list of available commands and their usage, you can use the help command:

```(hbnb) help```

## Examples
Here are some examples of how to use the command interpreter:

Create a new object:
```
(hbnb) create User
25e8bc5a-c946-4b04-9d27-85e90e2a9d62
(hbnb)
```
Show an object:
```
(hbnb) show User 25e8bc5a-c946-4b04-9d27-85e90e2a9d62
[User] (25e8bc5a-c946-4b04-9d27-85e90e2a9d62) {'id': '25e8bc5a-c946-4b04-9d27-85e90e2a9d62', 'created_at': '2023-03-08T14:25:36.661058', 'updated_at': '2023-03-08T14:25:36.661064'}
(hbnb)
```

Destroy an object:
```
(hbnb) destroy User 25e8bc5a-c946-4b04-9d27-85e90e2a9d62
(hbnb)
```
Show all objects:
```
(hbnb) all User
[]
(hbnb)
```
Update an object:
```
(hbnb) update User 25e8bc5a-c946-4b04-9d27-85e90e2a9d62 first_name "John"
(hbnb)
(hbnb) show User 25e8bc5a-c946-4b04-9d27-85e90e2a9d62
[User] (25e8bc5a-c946-4b04-9d27-85e90e2a9d62) {'id': '25e8bc5a-c946-4b04-9d27-85e90e2a9d62', 'created_at': '2023-03-08T14:25:36.661058', 'updated_at': '2023-03-08T14:29:05.582055', 'first_name': 'John'}
(hbnb)
```



