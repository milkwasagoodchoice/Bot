from typing import List
import sys


def get_triangle(rows: int) -> List[List[int]]:
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def print_triangle(triangle: List[List[int]]):
    for row in triangle:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python triangle.py <number_of_rows>")
        sys.exit(1)

    rows = int(sys.argv[1])
    triangle = get_triangle(rows)
    print_triangle(triangle)
