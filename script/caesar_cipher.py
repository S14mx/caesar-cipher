import nltk
from nltk.corpus import words


nltk.download("words", quiet=True)

word_list = words.words()


letters: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encrypt(string: str, key: int) -> str:
    output: str = ""
    split_input: list[str] = string.split()
    output_list: list[str] = []

    for word in split_input:
        for letter in word:
            if letter.lower() in letters:
                letter_idx: int = letters.index(letter.lower())
                shifted_letter_idx: int = (letter_idx + key) % 26
                if letter.isupper():
                    output += letters[shifted_letter_idx].upper()
                else:
                    output += letters[shifted_letter_idx]
            else:
                output += letter

        output_list.append(output)
        output = ""

    return " ".join(output_list)


def decrypt(string: str, key: str) -> str:
    return encrypt(string, -key)


def crack(string: str) -> str:
    key_dict: dict = {}
    split_input: list[str] = string.split()

    for word in split_input:
        for num in range(26):
            decrypt_attempt: str = decrypt(word, num)
            if decrypt_attempt.lower() in word_list:
                if num in key_dict:
                    key_dict[num] += 1
                else:
                    key_dict[num] = 1
                break

    if len(key_dict) > 0:
        key: int = max(key_dict, key=key_dict.get)
        if key_dict[key] >= len(split_input) // 2:

            return decrypt(string, key)

    return ""


if __name__ == "__main__":

    encrypt("bob 1!", 3)
    print(encrypt("It was the best of times, it was the worst of times.", 10))
    print(crack("Sd gkc dro locd yp dswoc, sd gkc dro gybcd yp dswoc!"))
    phrase = "Hello there!"
    print(decrypt(encrypt(phrase, 10), 10))
    print(crack(encrypt("All I know is that I don't know nothing", 25)))
