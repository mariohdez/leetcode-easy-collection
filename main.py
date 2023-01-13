from string_problems.string_to_integer import StringToInteger

def main() -> int:
    str = "-91283472332"
    test = StringToInteger()
    result = test.myAtoi(s=str)
    print(result)

    return 0

if __name__ == "__main__":
    main()
