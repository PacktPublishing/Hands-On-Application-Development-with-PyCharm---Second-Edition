from input.database_helper import write_to_database
import sqlite3
CANDY_DB = "candy.db"


def read_input_file_type_a(file_path: str) -> None:
    with open(file_path, "r") as data:
        for line in data:
            cleaned = line.strip("\n")
            write_to_database(cleaned)
    print("Processing Complete!")


def write_to_database(datum: str) -> None:
    connection = sqlite3.connect(CANDY_DB)
    cursor = connection.cursor()
    sql = f"INSERT INTO candy(name) VALUES ('{datum}')"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    read_input_file_type_a("../input_file_a.txt")
    