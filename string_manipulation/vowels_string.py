def main():
    strin = input("enter your string: ")
    chars = [*strin]
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    bean_counter = 0
    for char in chars:
        if char in vowel_list:
            bean_counter += 1
    print(bean_counter)
    return bean_counter

main()
