import sys

def is_feasible(books, n, k, mid):
    required_employees = 1
    current_load = 0

    for i in range(n):
        if books[i] > mid:
            return False

        if current_load + books[i] > mid:
            required_employees += 1
            current_load = books[i]
            if required_employees > k:
                return False
        else:
            current_load += books[i]

    return True

def find_optimal_workload(books, n, k):
    total_pages = sum(books)
    left = 0
    right = total_pages
    result = sys.maxsize

    while left <= right:
        mid = (left + right) // 2
        if is_feasible(books, n, k, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

def divide_books_among_employees(books, num_books, num_employees):
    optimal_workload = find_optimal_workload(books, num_books, num_employees)
    output_file = "output_data.txt"

    try:
        with open(output_file, "w") as file:
            file.write("The optimal division of books to minimize the maximum workload is:\n")

            current_load = 0
            current_employee = 1
            start_idx = 0

            for i in range(num_books):
                if current_load + books[i] > optimal_workload:
                    file.write(f"Employee {current_employee}: {current_load} pages ( ")
                    for j in range(start_idx, i):
                        file.write(f"{books[j]} ")
                    file.write(")\n")

                    current_load = books[i]
                    current_employee += 1
                    start_idx = i
                else:
                    current_load += books[i]

                if i == num_books - 1:
                    file.write(f"Employee {current_employee}: {current_load} pages ( ")
                    for j in range(start_idx, i + 1):
                        file.write(f"{books[j]} ")
                    file.write(")\n")

            file.write(f"The optimal division of books to minimize the maximum workload is: {optimal_workload} pages\n")
    except IOError:
        print("Error opening output file.")
