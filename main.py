import os
from book_division import divide_books_among_employees
from data_generation import test_data_generation, random_test_data_generation

def main():
    input_file = "input_data.txt"

    if not os.path.exists(input_file):
        print("Error opening input file.")
        return

    with open(input_file, "r") as file:
        num_employees = int(file.readline().strip())
        num_books = int(file.readline().strip())
        books = [int(file.readline().strip()) for _ in range(num_books)]

    divide_books_among_employees(books, num_books, num_employees)

    # Uncomment these lines to generate data for testing
    # test_data_generation()
    # random_test_data_generation()

if __name__ == "__main__":
    main()
