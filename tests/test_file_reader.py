
from tools.file_reader import RepositoryReader


def main():

    reader = RepositoryReader(".")

    print("\n===== REPOSITORY FILES =====")

    files = reader.list_files()

    for file in files:
        print(file)

    print("\n===== READING MAIN.PY =====")

    content = reader.read_file("main.py")

    print(content)

    print("\nRepository reader test completed!")


if __name__ == "__main__":
    main()
