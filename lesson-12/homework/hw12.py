#task1

import threading

# Shared list to collect primes (use a lock for thread safety)
prime_numbers = []
lock = threading.Lock()

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Thread worker function
def check_primes_in_range(start, end):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    # Add to shared list using lock
    with lock:
        prime_numbers.extend(local_primes)

# Main function
def main():
    start_range = 1
    end_range = 1000
    num_threads = 4

    # Calculate chunk size for each thread
    chunk_size = (end_range - start_range) // num_threads
    threads = []

    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes_in_range, args=(start, end))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort the result
    prime_numbers.sort()
    print("Prime numbers found:", prime_numbers)

if __name__ == "__main__":
    main()


#task2

import threading
from collections import Counter
import re

# Global dictionary to store total word counts
word_counts = Counter()
lock = threading.Lock()

# Function to clean and split lines into words
def tokenize(line):
    return re.findall(r'\b\w+\b', line.lower())

# Thread worker function
def process_lines(lines):
    local_counter = Counter()
    for line in lines:
        words = tokenize(line)
        local_counter.update(words)

    # Merge local results into global count safely
    with lock:
        word_counts.update(local_counter)

# Main function
def main():
    file_path = "large_text_file.txt"
    num_threads = 4

    # Read all lines from file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Divide lines among threads
    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=process_lines, args=(lines[start:end],))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print result
    print("Word Frequencies (Top 20):")
    for word, count in word_counts.most_common(20):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

