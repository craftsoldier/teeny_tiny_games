def main():
    input_string = input("enter the string to be reversed:   ")
    chars = [*input_string]
    reverse_chars = []
    for i in range(len(chars) - 1, -1, -1):
        reverse_chars.append(chars[i])
    reverse_string = "".join(reverse_chars)
    print(f"here's your string in reverse:     {reverse_string}")

main()
        
