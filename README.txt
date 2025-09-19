This web page runs with Flask.

It is used to input information about fictional library books into a form, which is then processed by the Python application to build a SQL query.

The SQL query is then used with the library_db database with MySQL, and its output is put into a table on the html page.

This is basically just a proof of concept.

---------------------------------------------------

Dependencies:

apache2
mysql
venv (Used to install Flask and mysql-connector-python under a virtual environment)
python3-flask
mysql-connector-python

Some .conf files for apache2 may need to be edited in order for this to work properly.

----------------------------------------------------

Setup:

//Install apache2:

$ sudo apt-get install apache2

//Install mysql:

$ sudo apt install mysql-server
$ sudo mysql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '************';
mysql> FLUSH PRIVILEGES;

//Install python modules:

$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install flask
$ pip3 install mysql-connector-python

//Set up library database:

mysql> source library_db/library_db.sql
Query OK, 1 row affected (0.19 sec)

Database changed
Query OK, 0 rows affected (1.40 sec)

Query OK, 35 rows affected (0.13 sec)
Records: 35  Duplicates: 0  Warnings: 0

//Setting up limited user 'Librarian':

//Set to desired password, not '********'
mysql> CREATE USER 'Librarian'@'localhost' identified by '********';
Query OK, 0 rows affected (0.16 sec)

mysql> source library_db/library_db.sql
Query OK, 1 row affected (0.13 sec)

Database changed
Query OK, 0 rows affected (1.56 sec)

Query OK, 35 rows affected (0.12 sec)
Records: 35  Duplicates: 0  Warnings: 0

mysql> GRANT select ON library_db.* TO 'Librarian'@'localhost';
Query OK, 0 rows affected (0.12 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| library_db         |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

mysql> show grants for 'Librarian'@'localhost';
+-----------------------------------------------------------+
| Grants for Librarian@localhost                            |
+-----------------------------------------------------------+
| GRANT USAGE ON *.* TO `Librarian`@`localhost`             |
| GRANT SELECT ON `library_db`.* TO `Librarian`@`localhost` |
+-----------------------------------------------------------+
2 rows in set (0.00 sec)

//Run commands to copy files to correct directory and change permissions:

$ sudo cp library_db.py /var/www/html/library_db.py; 
$ sudo chmod 755 /var/www/html/library_db.py; 
$ sudo cp library_db.html /var/www/html/templates/library_db.html; 
$ sudo chmod 755 /var/www/html/templates/library_db.html; 
$ sudo cp library_db.css /var/www/html/static/library_db.css; 
$ sudo chmod 755 /var/www/html/static/library_db.css;

//Activate myenv, then run the Flask app:
$ source myenv/bin/activate; 
$ python3 /var/www/html/library_db.py
//CTRL + c to close application

//Afterwards (For venv):
$ deactivate
