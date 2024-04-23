import csv
import os

def merge_csv_files(*paths, delimiter=';', only_shared_columns=False):
    if not paths:
        raise ValueError("At least one file path must be provided.")

    for path in paths:
        if not os.path.isfile(path):
            raise ValueError(f"{path} is not a valid file path.")
    data = []
    header_set = []

    for path in paths:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=delimiter)
            for header in csv_reader.fieldnames:
                if header not in header_set:
                    header_set.append(header)
            data.extend(list(csv_reader))

    if not only_shared_columns:
        # Fill empty values with "NaN"
        for row in data:
            for col in header_set:
                row[col] = row.get(col, 'NaN')

    output_filename = 'merged_shared.csv' if only_shared_columns else 'merged.csv'
    output_path = os.path.join(os.path.dirname(paths[0]), output_filename)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=header_set, delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(data)

merge_csv_files('ultratest/ex3_1.csv', 'ultratest/ex3_2.csv', 'ultratest/ex3_3.csv', delimiter=';', only_shared_columns=False)
merge_csv_files('ultratest/ex3_1.csv', 'ultratest/ex3_2.csv', 'ultratest/ex3_3.csv', delimiter=';', only_shared_columns=True)