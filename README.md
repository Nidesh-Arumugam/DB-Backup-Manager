# DB-Backup-Manager

> The backup manager is used to take the back up of the data bases mentioned by the user

> Here, we are writing the code to take the backup of SQL database  based on the inputs provided by the user

> We will be getting the inputs of IP, PORT, DBName, UserName and Password of the sql Database

> Once all the validations are done, the backup have been initialized in  the specified folder.


# Core

> core is the basic app , where all the backup codings and API's are carried out

> The management/command inside the core folder consist of the command that can be used on the terminal for backup process

> python manage.py dbcommand

> The backup can be triggered manully by using this command on the terminal or by using the DB form on the browser


# Templates

> The template folder consist of  all the  HTML pages which can be used as an frontend for our Django project

# Account

> This App consist of all the contents required for the validation purposes, it contains the coding for user login ,log out and throw an error message if invalid contents have been used. 
