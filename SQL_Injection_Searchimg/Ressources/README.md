# SQL Injection on Searchimg page

## Description 
SQL Injection (SQLi) is a web security vulnerability where attackers manipulate SQL queries executed by an application to gain unauthorized access to a database. This can lead to data theft, modification, or even full control of the database server.

## BornToSec
Here on the search searchimg page you have an input which is asking for an ID. If you input an id and submit, you will see in the URL that the id is passed as a parameter. This is a good sign that the application is vulnerable to SQL Injection.

To get all the images we need to give a conditions to the query that will always be true. We can do this by using the OR 1=1 statement. This will return all the images in the database.

```
http://10.11.249.222/index.php?page=searchimg&Submit=Submit&id=5 OR 1=1
```

With this, you will get the list of every images in the table.

Then what we want is to get more informations about the image table and the columns but to do this we first need to discover the name of the table.

```
http://10.11.249.222/index.php?page=searchimg&Submit=Submit&id=5 UNION SELECT NULL, table_name FROM information_schema.tables
```

With this query, we are able to get the name of every tables in the database. We can see that the table list_images is present.

We would now wanted to get the columns of the list_images table by using the following query.

```
http://10.11.249.222/index.php?page=searchimg&Submit=Submit&id=5 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name='list_images'
```

As you see, we are not able to send string in the query so we need to use the CHAR function to send the table name.

l → 108
i → 105
s → 115
t → 116
_ → 95
i → 105
m → 109
a → 97
g → 103
e → 101
s → 115

CHAR(108, 105, 115, 116, 95, 105, 109, 97, 103, 101, 115)

Now we can get the columns of the list_images table.

```
http://10.11.249.222/index.php?page=searchimg&Submit=Submit&id=10 UNION SELECT NULL, column_name FROM information_schema.columns WHERE table_name=CHAR(108, 105, 115, 116, 95, 105, 109, 97, 103, 101, 115)
```

Once we have the columns, we can get the data of the list_images table. We can see columns id, url, title, comment.

The one that is interesting is comment. We can get the data of this column by using the following query.

```
http://10.11.249.222/index.php?page=searchimg&Submit=Submit&id=5 UNION SELECT id, comment FROM list_images
```

With this query, we are able to get the comment of the image with the id 5. We can see that the comment of the user with id=5 is "If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46".

Now we can use a md5 decrypter to get the word albatroz.
Then we use sha256 on albatroz and we get the flag.


