from tasks import task2, task5, task6, task3, task1, task4, task7, task8, task9


def main():
    test1a = 'some stringaA'
    print(F"Count 'a' in string '{test1a}': {task1.count_letter('a', test1a)}")

    test1s = 'some stringa'
    print(F"Count 's' in string '{test1s}': {task1.count_letter('s', test1s)}")

    test2 = 'some strIng hEre and nOw'
    print(F"\nCount vowel in string '{test2}': {task2.count_vowel(test2)}")

    test3 = "Some text here"
    print(F"\nReverse string '{test3}' with arr slice: {task3.revert_arr_slice(test3)}")
    print(F"Reverse string '{test3}' with slice: {task3.revert_slice(test3)}")
    print(F"Reverse string '{test3}' with range: {task3.revert_range(test3)}")

    array0 = ['a', 1, 'b', 2, 'c', 8]

    print(F"\nReverse array {array0} with slice: {task4.revert_reverse(array0.copy())}")
    print(F"Reverse array {array0} with arr slice: {task4.revert_arr_slice(array0)}")
    print(F"Reverse array {array0} with arr slice: {task4.revert_range(array0)}")

    array0 = [1, 2, 3, 4, 5]
    print(F"\nSwap elements in array {array0}: {task5.swap_first_last(array0)}")
    # print(F"Swap elements in array {[0]}: {task5.swap_first_last([0])}") # function throws exception

    array0 = ['we', 'aaaaaa', 'zzzzz', 'sddd']
    print(f"\nMake eq length elements of {array0}: {task6.make_eq_length(array0)}")

    dict_one = {'a': 100, 'b': 200}
    dict_two = {'c': 300, 'd': 400}
    print(f"\nCombination of two dictionaries {dict_one} and {dict_two} "
          f"is: {task7.combine_dicts(dict_one, dict_two)}")

    dict_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(f"\nSum of dict {dict_numbers} values is: {task8.prod_values(dict_numbers)}")

    array1 = array0.copy()
    print(f"\nArrays {array0} and {array1} merged into dictionary: {task9.lists_to_dict(array0, array1)}")

    set1 = {0, 1, 4, 2}
    set2 = {1, 9}
    set3 = {2, -5}


if __name__ == "__main__":
    main()
