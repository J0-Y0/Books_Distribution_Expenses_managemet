## Next Todo
 1. Authoriztione( user group level)
    - User
          - view except users 
          - CRUD Books
    - Admin
         all+CRUD User
2. profile size compretion or limiting
    - change the default image too,
3. change the login layout
4. make it responsive to mobile view  
     
     
    






# Books_Distribution_Expenses

Books Distribution Expenses Tracker app build by Django python framework

# Data model

    1. Books
       -  [id ,title,subtitle, author, publisher . . .category ,modification_log ]
       -  id -> unique number
       - category field[type] related to category model field
    2. Category
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

    - user crud
    - username change
    - self password edit
    - admin  as a staff user |as an option
    - category - - - as un-categorized





    1. User Groupe
    2. Authentication
    4. user crud

# task done

    1.Optimize CRUD templates context
    2.back button
        - delete : auto bach----doen
        - edit : auto back---done
    3.add : via cancel / add next
    4.pagination
        <1 ..40 41 42 ...100>-----done
    3.icon and style for the CRUD----done
