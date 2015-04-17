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
                     user="opennirv_php", 
                      passwd="}wWkNzI6A-N7", 
                      db="opennirv_rma")

Step 6: Change the Path here ("f" this is the folder where all files are created so it write permission 777)
"admin/makehtml.py"
create_file = '/home6/opennirv/public_html/beta/form_builder/admin/f/'
copy_file = '/home6/opennirv/public_html/beta/form_builder/admin/'

Step 7: Change the Path "admin/form_python.php"
Line no :- 43
$command = "/home6/opennirv/python27/Python-2.7.4/python /home6/opennirv/public_html/beta/form_builder/admin/testme.py";


