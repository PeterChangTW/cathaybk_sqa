def sort_odd_even(num_list):
    # split odd and even numbers
    odd_numbers = [num for num in num_list if num % 2 != 0]
    even_numbers = [num for num in num_list if num % 2 == 0]

    # sort number for ascending
    even_numbers.sort()

    # sort number for descending
    odd_numbers.sort(reverse=True)

    # put odd numbers first
    sorted_numbers = odd_numbers + even_numbers

    return str("".join([str(num) for num in sorted_numbers]))

numbers = [int(char) for char in input("請輸入數字：")]
print("排序結果為", sort_odd_even(numbers))
