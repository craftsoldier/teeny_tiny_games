def main():
    morse_alphabet = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
    }

    morse_numbers = {
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    morse_punctuation = {
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

    text_input = input("enter text for conversion:   ")

    chars = [*text_input]
    morse_output = []

    for char in chars:
        if char == ' ':
            morse_output.append('/')
        elif char.upper() in morse_alphabet:
            morse_output.append(morse_alphabet[char.upper()])
        elif char in morse_numbers:
            morse_output.append(morse_numbers[char])
        elif char in morse_punctuation:
            morse_output.append(morse_punctuation[char])

    print(' '.join(morse_output))

main()
