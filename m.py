import psycopg2
def market():
    mar=psycopg2.connect(
        host='localhost',
        database="market",
        user="postgres",
        password="ulugbek"
    )
    return mar