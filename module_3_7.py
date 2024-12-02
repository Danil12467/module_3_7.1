def calculate_structure_sum(*args):
    total_sum = 0

    for data in args:
        if isinstance(data, list):
            for item in data:
                total_sum += calculate_structure_sum(item)

        elif isinstance(data, dict):
            for key, value in data.items():
                total_sum += len(key)
                total_sum += calculate_structure_sum(value)

        elif isinstance(data, tuple):
            for item in data:
                total_sum += calculate_structure_sum(item)

        elif isinstance(data, str):
            total_sum += len(data)

        elif isinstance(data, (int, float)):
            total_sum += data

        elif isinstance(data, (set)):
            total_sum += len(data)


    return total_sum

result = calculate_structure_sum(
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]),  # Более сложная вложенная структура
)

print(result)