import numpy as np
import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    entries = content.strip().split('%')
    parsed_data = []
    for i, entry in enumerate(entries):
        print(f"Parsing Entry {i + 1}: {entry}")  # Вывод текущей записи
        matches = re.findall(r"([A-Z])=\(([\d\s\-;]+)\)", entry)
        print(f"Matches found: {matches}")  # Вывод результата регулярного выражения
        if matches:
            parsed_entry = {
                name: np.array([list(map(float, row.split())) for row in data.split(';')])
                for name, data in matches
            }
            parsed_data.append(parsed_entry)
        else:
            print(f"Warning: No valid matrices or vectors found in entry: {entry}")
    return parsed_data

def to_upper_triangular(matrix):
    n = len(matrix)
    mat = matrix.copy()
    for i in range(n):
        max_row = i + np.argmax(abs(mat[i:, i]))
        mat[[i, max_row]] = mat[[max_row, i]]
        if mat[i, i] == 0:
            continue
        for j in range(i + 1, n):
            factor = mat[j, i] / mat[i, i]
            mat[j, i:] -= factor * mat[i, i:]
    return mat

def determinant(matrix):
    upper_tri = to_upper_triangular(matrix)
    det = np.prod(np.diag(upper_tri))
    return det

def rank(matrix):
    upper_tri = to_upper_triangular(matrix)
    return np.sum(np.abs(np.diag(upper_tri)) > 1e-10)

def inverse(matrix):
    n = len(matrix)
    augmented = np.hstack((matrix, np.eye(n)))
    for i in range(n):
        max_row = i + np.argmax(abs(augmented[i:, i]))
        augmented[[i, max_row]] = augmented[[max_row, i]]
        if augmented[i, i] == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        augmented[i] /= augmented[i, i]
        for j in range(n):
            if j != i:
                augmented[j] -= augmented[j, i] * augmented[i]
    return augmented[:, n:]

def solve_system(matrix, vector):
    n = len(matrix)
    augmented = np.hstack((matrix, vector.reshape(-1, 1)))
    for i in range(n):
        max_row = i + np.argmax(abs(augmented[i:, i]))
        augmented[[i, max_row]] = augmented[[max_row, i]]
        if augmented[i, i] == 0:
            continue
        augmented[i] /= augmented[i, i]
        for j in range(n):
            if j != i:
                augmented[j] -= augmented[j, i] * augmented[i]
    solution = augmented[:, -1]
    return solution

def kronecker_capelli(matrix, vector):
    rank_a = rank(matrix)
    augmented_matrix = np.hstack((matrix, vector.reshape(-1, 1)))
    rank_augmented = rank(augmented_matrix)
    return rank_a == rank_augmented, rank_a == rank(matrix)

def process_entry(entry):
    result = []
    if 'A' not in entry:
        return "Error: Missing matrix 'A'."
    
    if 'B' in entry:
        A = entry['A']
        B = entry['B'].flatten()
        consistent, unique = kronecker_capelli(A, B)
        if not consistent:
            result.append("The system is inconsistent.")
        elif unique:
            solution = solve_system(A, B)
            result.append(f"Unique solution: {solution}")
        else:
            result.append("The system has infinitely many solutions.")
    else:
        A = entry['A']
        result.append(f"Determinant: {determinant(A)}")
        result.append(f"Rank: {rank(A)}")
        try:
            inv = inverse(A)
            result.append(f"Inverse matrix:\n{inv}")
        except ValueError:
            result.append("Matrix is singular and cannot be inverted.")
    return '\n'.join(result)

def main(input_file, output_file):
    entries = parse_input(input_file)
    results = []
    for i, entry in enumerate(entries):
        results.append(f"Entry {i + 1}:")
        results.append(process_entry(entry))
        results.append('\n')
    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

if __name__ == "__main__":
    input_file = "input46.txt"
    output_file = "output46.txt"
    main(input_file, output_file)
