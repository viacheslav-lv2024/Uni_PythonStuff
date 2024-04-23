import csv
import os

def merge_csv_files(*paths, delimiter=';', only_shared_columns=False):
    if not paths:
        raise ValueError("At least one file path must be provided.")

    for path in paths:
        if not os.path.isfile(path):
            raise ValueError(f"{path} is not a valid file path.")
    data = []
    header_set = set()

    for path in paths:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=delimiter)
            header_set.update(csv_reader.fieldnames)
            data.extend(list(csv_reader))

    if only_shared_columns:
        shared_columns = set(header_set)
        data = [{col: row.get(col, '') for col in shared_columns} for row in data]

    output_path = os.path.join(os.path.dirname(paths[0]), 'merged.csv')
    with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=header_set, delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(data)

merge_csv_files('ultratest/ex3_1.csv', 'ultratest/ex3_2.csv', 'ultratest/ex3_3.csv', delimiter=';', only_shared_columns=False)