#!/usr/bin/env python3

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

# Creating an empty dictionary to be used later in the create_dictionary function.
result_dict = {}

def create_dictionary(keys, values):
    # Using a counter variable to iterate over the provided keys and values.
    counter = 0
    # Iterating over the keys and values to populate the result dictionary.
    while counter < len(keys):
        result_dict[keys[counter]] = values[counter]
        counter += 1
    return result_dict

# Defining a function to find common values between two dictionaries.
def shared_values(dict1, dict2):
    # Extracting the values from both dictionaries.
    dict1_values = dict1.values()
    dict2_values = dict2.values()
    # Converting the values into sets to find common values.
    set1 = set(dict1_values)
    set2 = set(dict2_values)
    return set1.intersection(set2)
if __name__ == "__main__":
    york = create_dictionary(list_keys, list_values)
    print("York: ", york)
    common = shared_values(dict_york, dict_newnham)
    print("Shared Values:", common)

