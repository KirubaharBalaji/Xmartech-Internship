
import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            database="mydb",
            user="postgres",
            password="0203",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False


web_url = 'https://atozserver.com'
web_name = 'atozserver'
web_sitemap = 'https://atozserver.com/sitemap.xml'
conn = get_connection()
cursor = conn.cursor()
if conn:
    print("Connection to the PostgreSQL established successfully.")
   # cursor.execute(
#    f"insert into mytable(website_name,website_url,website_sitemap) values({web_name},{web_url},{web_sitemap})")
    cursor.execute(
        f"insert into mytable(website_name,website_url,website_sitemap) values('atozserver','https://atozserver.com','https://atozserver.com/sitemap.xml')")
    cursor.execute('SELECT * FROM mytable;')

    rows = cursor.fetchall()
    # Make the changes to the database persistent
    print(rows)
    conn.commit()
    # Close cursor and communication with the database
    cursor.close()
    conn.close()
else:
    print("Connection to the PostgreSQL encountered and error.")
