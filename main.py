import task1
import task2
import task3
import task4
import task5


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

    array = ['a', 1, 'b', 2, 'c', 8]

    print(F"\nReverse array {array} with slice: {task4.revert_reverse(array.copy())}")
    print(F"Reverse array {array} with arr slice: {task4.revert_arr_slice(array)}")
    print(F"Reverse array {array} with arr slice: {task4.revert_range(array)}")

    array = [1, 2, 3, 4, 5]
    print(F"Swap elements in array {array}: {task5.swap_first_last(array)}")
    # print(F"Swap elements in array {[0]}: {task5.swap_first_last([0])}")


if __name__ == "__main__":
    main()
