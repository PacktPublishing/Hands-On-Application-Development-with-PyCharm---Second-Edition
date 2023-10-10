import sqlite3

from input.read_input_file_a import CANDY_DB


def write_to_database(datum: str) -> None:
    connection = sqlite3.connect(CANDY_DB)
    cursor = connection.cursor()
    sql = f"INSERT INTO candy(name) VALUES ('{datum}')"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    connection.close()
    