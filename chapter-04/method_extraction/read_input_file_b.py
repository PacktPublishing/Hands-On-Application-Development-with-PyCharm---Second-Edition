import json
from read_input_file_a import write_to_database


def read_input_file_type_b(file_path: str) -> None:
    with open(file_path, "r") as json_data:
        data = json.load(json_data)
        candies = data["data"]
        for candy in candies:
            write_to_database(candy)

    print("Processing Complete!")


if __name__ == "__main__":
    read_input_file_type_b("../input_file_b.json")
    