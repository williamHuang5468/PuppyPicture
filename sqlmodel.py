import psycopg2

def create_table():
    try:
        conn = connect()
        cursor = conn.cursor()

        # user id PRMIARY KEY, username unike
        cursor.execute("CREATE TABLE puppytable (id SERIAL PRIMARY KEY, slug char(32), name char(32), image_url char(128));")

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def create_puppy(slug, name, image_url):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO puppytable (slug, name, image_url) VALUES (%s, %s, %s)", (slug, name, image_url))

        cursor.execute("SELECT * from puppytable")
        row = cursor.fetchall()
        print(row)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def read_all():
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from puppytable")
        row = cursor.fetchall()
        print(row)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def read(slug):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from puppytable WHERE puppytable.slug = '"+ slug + "'")
        row = cursor.fetchone()
        print(row)
        conn.commit()
        cursor.close()
        conn.close()
        return row
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def connect():
    connect_str = "dbname=puppydb user=william host=localhost " + \
                  "password=wflu"
    conn = psycopg2.connect(connect_str)
    return conn

