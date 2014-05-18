def validate_nonogram(nonogram, keys):
    is_correct = []
    for index in range(len(nonogram)):
        filled_squares_number = nonogram[index].count('X')
        is_correct.append(filled_squares_number == sum(keys['rows'][index]))

    transposed_nonogram = [list(x) for x in zip(*nonogram)]
    for index in range(len(transposed_nonogram)):
        filled_squares_number = transposed_nonogram[index].count('X')
        is_correct.append(filled_squares_number == sum(keys['columns'][index]))

    return all(is_correct)