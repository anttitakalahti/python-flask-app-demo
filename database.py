import numpy
import os
import psycopg2

DATABASE_URL = os.environ["DATABASE_URL"]

"""
    check credentials from heroku

    CREATE TABLE images (
        image_id SERIAL PRIMARY KEY,
        pixels TEXT NOT NULL,
        label INT NOT NULL,
        created TIMESTAMPTZ DEFAULT NOW()
    );
"""


def store_image_with_label(pixels: numpy.ndarray, label: int) -> int:
    # http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries
    sql = "INSERT INTO images (pixels, label) VALUES (%s, %s) RETURNING image_id;"

    image_id = 0
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cur = conn.cursor()

        cur.execute(sql, (pixels.tostring(), label))

        image_id = cur.fetchone()[0]

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

    return image_id
