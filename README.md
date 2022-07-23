# Python GUI note-taking app

## Learning summary

While learning the Tkinter GUI framework for Python, I have produced a note-taking app as one of my projects. This project features a user account system, where users can create accounts and log into the application. Within the application they can write notes and save those notes to a database so that they can be accessed the next time they log in.

* Python programming language: while already knowing basic Python syntax prior to this project, I have learned more complicated and less prevalent Python syntax and concepts. For instance, the `**kwargs` arguments in functions, or the `__new__()` method and `cls` keyword within class definitions.

* Tkinter: since the front end of this project is made with Tkinter, I have learned how to construct and style GUIs from design to reality using this framework. Beyond learning about the basics of Tkinter widgets and some basic options, I learned much more obscure functionality, such as binding custom events to functions, simulating events, validation functions for entries and more.

* Object-oriented programming: while working on this project, I learned how to use OOP design more ubiquitously throughout the design of the solution. Since the app is a GUI app, it naturally lends itself to the OOP paradigm, to the point where both the main window and all the individual scenes were all objects. I further used OOP concepts like inheritance to define base functionality of `Scene` components (which themselves inherited the Tkinter `Frame`) and could be inherited by individual scene classes to draw anything to screen — managed by the `Main` app class. Furthermore, I learned the power of polymorphism. I declared empty methods in super-classes (like `on_show()` and `on_hide()` methods) which could be overridden in sub-classes to enable things like optional callback functionality. Continuing the theme of learning OOP, I even used object-oriented patterns in my project, such as the Singleton pattern for the `DatabaseAccess` class, as I only wanted one persistent object accessing and modifying the user database during program runtime.

* SQL database: this project utilised an SQL database (the `sqlite3` module for Python) to store user data. Logging in required querying the database with the `SELECT` keyword, creating an account involved creating records with the  `INSERT INTO` syntax, saving the user's notes required modifying the values within the database with the `UPDATE` keyword and finally, deleting an account meant I had to delete the appropriate record from the database with the `DELETE FROM` syntax.

* Security: since this project features things like user's passwords and their private notes, I needed to secure those from potential bad actors when storing them in the database. I learned about and implemented password hashing and salting: storing the resulting hash in the database rather than the password itself, to keep the user password secure. I also used an implementation of a symmetric encryption cipher, called AES, to encrypt the user notes (which may potentially be sensitive) and stored the resultant ciphertext, rather than plaintext,  in the database. This data could then be read and securely decrypted by the app if the appropriate user logged in.

* Problem-solving: I used Tkinter for the front end of this project. Tkinter doesn't by default support switching between multiple scenes, so this functionality had to be created by me. I used the idea of passing-by-reference callback functions to solve the problem. Each scene would emit an `Action`, captured by an `ActionListener`, which would call a function within the `Main` class to deal with this action. One of the ways to deal with this `Action` was to perform scene switching. This way, I could wire up scenes to switch between each other if need be.

## How to operate this project

### How to run the project

1. Make sure you have the Python interpreter installed.
2. Clone this repository.
4. Run the `run` file.

### Application use

To start taking notes, you must either sign up or log into an already existing account. You will then be able to edit and save your notes for that account. The account can be deleted (once logged in), and all the notes will be deleted along with the account.

## Viewing and  modifying  the project

This repository is wasn't editited in a specialised code editor - so doesn't have any code-editor-specific artefacts. Hence, it can be cloned and edited in any text editor of your chosing.
