from m import market

marcet=market()
cur=marcet.cursor()
marcet.autocommit=True

# cur.execute(
#     "CREATE DATABASE Market"
# )
# print("database yaratildi")


# cur.execute(
#     """
#     CREATE TABLE marketing(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price NUMERIC(10,2)
#     )
#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO marketing(name,price) VALUES('docha',15000) , ('banan',12000) , ('qulupnay',16000) , ('shaftoli',12000), ('anjir',11000), ('sholtut',10000), ('kiwi',19000)" ,

# )
# print("+")

# cur.execute(
#     "DELETE FROM marketing WHERE ID='8'"
# )
# print('-')


# cur.execute(
#     "SELECT * FROM marketing  ORDER BY name"
# )

# cur.execute(
#     "SELECT * FROM marketing  WHERE name ILIKE 'A%'"
# )

# cur.execute(
#     "SELECT * FROM marketing WHERE price >= 15000"
# )

# cur.execute(
#     "SELECT * FROM marketing LIMIT 3"
# )



# rows=cur.fetchall()
# for row in rows:
#     print(row)