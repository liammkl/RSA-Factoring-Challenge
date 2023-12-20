#!/usr/bin/env python3

import sys
import time

def factorize(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

def format_output(num, factors):
    return f"{num}={'*'.join(map(str, factors))}"

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            factors = factorize(num)
            output = format_output(num, factors)
            print(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factors <filename>")
        sys.exit(1)

    start_time = time.time()
    main(sys.argv[1])
    end_time = time.time()

    print("\nExecution time:", round(end_time - start_time, 3), "seconds")
