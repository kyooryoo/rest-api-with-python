import sqlite3

# create a DB, connect it, and prepare to access it
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# create a table by defining a query and executing it
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# create a user tuple, an insert query and execute it
user = (1, 'Amy', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# create a list of users, and insert it by calling the query
users = [
    (2, 'Bill', 'asdf'),
    (3, 'Carry', 'asdf')
]
# pay attention to the function of executemany() here
cursor.executemany(insert_query, users)

# create a select query and print each row selected
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# commit the change to the DB and close the connection
connection.commit()
connection.close()