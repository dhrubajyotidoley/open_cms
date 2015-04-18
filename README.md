This is Free CMS in HTML, PHP and MySQL

Here we have used Python to generate PHP files on the admin folder

---------------------------------------------------------------------

Folder Structure

cms
   admin
   css
   fonts
   images
   include
   js
      --index.php
      --cms.sql

----------------------------------------------------------------------

Database
cms.sql
This is the database with the table users_admin

----------------------------------------------------------------------

Step 1: Create Database

Step 2: Import cms.sql

Step 3: Change the database details on "include/config.php"

Step 4: Login to Admin "admin/index.php"
username: admin
password: admin

Step 5: Add database credential to "admin/makehtml.py"
Line No :- 287
db = MySQLdb.connect(host="localhost", 
                     user="username", 
                      passwd="password", 
                      db="dbname")


Step 6: Add database credential to "admin/testme.py"
Line No :- 154
dbnew = MySQLdb.connect(host="localhost", 
                     user="username", 
                      passwd="password", 
                      db="dbname")

Step 7: Create a Folder "f" on the server under the "admin" directory
change the permission to 777

Step 8: Change the Path here ("f" this is the folder where all files are created so it write permission 777)
"admin/makehtml.py"
create_file = '/PATH_TO_ADMIN_FOLDER/admin/f/'
copy_file = '/PATH_TO_ADMIN_FOLDER/admin/'

Step 9: Change the Path "admin/form_python.php"
Line no :- 43
$command = "python /PATH_TO_ADMIN_FOLDER/admin/testme.py";
