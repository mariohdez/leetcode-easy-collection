from string_problems.first_unique_char_in_a_str import FirstUniqueCharacterInString

def main() -> int:
    str = "loveleetcode"
    test = FirstUniqueCharacterInString()
    result = test.firstUniqChar(s=str)
    print(result)

    return 0

if __name__ == "__main__":
    main()
