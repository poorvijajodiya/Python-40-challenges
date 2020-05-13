print("\t\tSummary table")
num_strings = ["15", "100", "55", "42"]
num_ints = [15,100,55,42]
num_floats = [15.4, 33.8, 98.4, 76.9]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]
print("\nThe variable num string is a {}.\nIt contains the element: {}.\nthe element {} is a {}".format(type(num_strings), num_strings,num_strings[0], type(num_strings[0])))
print("\nThe variable num ints is a {}.\nIt contains the element: {}.\nthe element {} is a {}".format(type(num_ints), num_ints, num_ints[0], type(num_ints[0])))
print("\nThe variable num floats is a {}.\nIt contains the element: {}.\nthe element {} is a {}".format(type(num_floats), num_floats,num_floats[0], type(num_floats[0])))
print("\nThe variable num lists is a {}.\nIt contains the element: {}.\nthe element {} is a {}".format(type(num_lists), num_lists,num_lists[0], type(num_lists[0])))
print("\nNow sorting num lists and num strings are...\n sorted num_strings: {}\n sorted num_ints: {}".format(sorted(num_strings), sorted(num_ints)))
print()
print("Strings are sorted alphabetically while integers are sorted numerically!")