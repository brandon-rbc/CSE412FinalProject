# FilmFriend User Manual
_FilmFriend_ is an application designed to let users track and favorite different movies and TV shows they've watched. Users can search for media by name, genre, and director, and can keep track of media by having a favorites list. 


1. [App Setup](#setupinstallation)
2. [App Tutorial](#tutorialhow-to-use)

# Setup/Installation - Windows
To set up FilmFriend, you must first install the required packages and necessary components. 
This includes **Python 3.8**, **PostgreSQL**, and **PyCharm6**, as well as the core FilmFriend files. 
1. [Set up Dependencies](#dependencies)
2. [Set up the Files](#files)


## Dependencies
You must first install the following dependencies before running this software:
 1. Python(3.8)
 2. PostgreSQL(12.4+)
 3. PyQT5 (5.15.1)
 4. 

After installing the dependencies, open up a window of Windows PowerShell. 
In PowerShell, begin by typing
```
> cd "(your install location)\PostgreSQL\14\bin"
```
If you installed it in the default location, the exact line to run would be
```
> cd "C:\Program Files\PostgreSQL\14\bin"
```
Then, set the environment variables PGHOST and PGPORT. 
Still in PowerShell, type
```
> set PGHOST=/tmp
```
and
```
> set PGPORT=5432
```

## Files
Open PyCharm. 
Click "Get from VCS" and install Git if it has not already been installed. 
Then, copy and paste the link to our repository (https://github.com/brandon-rbc/CSE412FinalProject) where it says "URL:"
Click Clone. You may be asked to log into GitHub. If so, click "Log in with GitHub," and then click the Authorize button when the new page is opened. 

Now, go to the folder you cloned the repository to. If you left it default, it should be C:\Users\(your username)\PycharmProjects\CSE412FinalProject 
In this folder, create a new folder called "database". 
Once you do this, go back to PowerShell and run the following command: 
```
> .\initdb C:\Users\(your username)\PycharmProjects\CSE412FinalProject\database
```
After initializing the database (you just did this), run the following command to start the database: 
```
> .\pg_ctl -D C:\Users\(your username)\PycharmProjects\CSE412FinalProject\database -o '-k /tmp' start
```

# Tutorial/How to Use
Now that you've installed the app, here's an overview of how to use FilmFriend. 

We'll break this down into a few sections.

1. [Browsing](#browsing)
2. [Searching](#searching)
3. [Favoriting](#favoriting)

## Browsing

## Searching

## Favoriting
