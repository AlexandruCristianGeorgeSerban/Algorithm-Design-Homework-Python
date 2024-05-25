import random
import time

def generate_and_save_books(num_books):
    books = [100 * (i + 1) for i in range(num_books)]
    with open("book_data.txt", "w") as file:
        for book in books:
            file.write(f"{book}\n")

def generate_and_save_random_books(num_books):
    random.seed(time.time())
    books = [random.randint(1, 100000000) for _ in range(num_books)]
    with open("random_book_data.txt", "w") as file:
        for book in books:
            file.write(f"{book}\n")

def test_data_generation():
    num_books = int(input("Enter the number of books for data generation: "))
    generate_and_save_books(num_books)
    print("Book data has been generated and saved to book_data.txt\n")

def random_test_data_generation():
    num_books = int(input("Enter the number of books for random data generation: "))
    generate_and_save_random_books(num_books)
    print("Random book data has been generated and saved to random_book_data.txt\n")
