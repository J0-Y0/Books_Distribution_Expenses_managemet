# Books_Distribution_Expenses

Books Distribution Expenses Tracker app build by Django python framework

# Data model

    1. Books
       -  [id ,title,subtitle, author, publisher . . .category ,modification_log ]
       -  id -> unique number
       - category field[type] related to category model field
    2. category
        - [type,added_by ]
    3.User
        - [username,email,password,user_groupe,invited_by]
        - invited_by field
            record who add this user to the system

# User Groupe

        a. User
            - can  CRUD (create, read, update delete) for Books
        b. Admin
            - can do every thing what a user can do plus
            - can  CRUD (create, read, update delete) for Users i.e user management
            - can access django administration

# who can access to the system

    For security purpose user can not create their account ,they only invited by the the system admin.
    and then when they first time to  login they forward to password change form

# modification log

    -date
    -user
    -action
    -description

# next todo

    1.Optimize CRUD templates context
    2.back button
        - delete : auto bach
        - edit : auto back
        - add : via cancel / add next
    3.icon and style for the CRUD
