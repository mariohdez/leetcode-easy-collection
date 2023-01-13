class StringToInteger:
    def myAtoi(self, s: str) -> int:
        result = 0
        i = 0
        sign = '+'
        MAX = 2147483647
        MIN = -2147483648

        while i < len(s) and s[i].isspace():
            i = i + 1

        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = s[i]
            i = i + 1

        while i < len(s) and s[i].isnumeric():
            digit = int(s[i])

            if (result > MAX // 10) or (result == MAX // 10 and digit > 7):
                return MAX if sign == '+' else MIN

            result = (result * 10) + digit

            i = i + 1

        if sign == '-':
            result = result * -1

        return result