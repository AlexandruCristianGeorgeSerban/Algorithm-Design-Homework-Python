.PHONY: all run generate generate_random clean

all: run

run:
	@echo "Running the main program..."
	python3 main.py

generate:
	@echo "Generating book data..."
	python3 -c "from data_generation import test_data_generation; test_data_generation()"

generate_random:
	@echo "Generating random book data..."
	python3 -c "from data_generation import random_test_data_generation; random_test_data_generation()"

clean:
	@echo "Cleaning up generated files..."
	rm -f book_data.txt random_book_data.txt output_data.txt input_data.txt
