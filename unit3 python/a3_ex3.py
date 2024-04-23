input_string = input('Enter comma-separated elements: ')
list_of_strings = input_string.split(",")
hash_val = 0
dictionary_of_hash_values = {}

for string_part in list_of_strings:
    for element in string_part:
        hash_val += ord(element)
    if string_part in dictionary_of_hash_values:
        assert hash_val == dictionary_of_hash_values[string_part]
    dictionary_of_hash_values.update({string_part: hash_val})
    hash_val = 0

for dict_key in dictionary_of_hash_values:
    print(f"'{dict_key}'", "->", dictionary_of_hash_values[dict_key])