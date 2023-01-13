class StrStr:
    def strStr(self, haysack: str, needle: str) -> int:
        i = 0
        haystackLen = len(haysack)
        needleLen = len(needle)

        while i < haystackLen:
            j = 0

            while (i + j) < haystackLen and j < needleLen and haysack[i+j] == needle[j]:
                j = j + 1

            if j == needleLen:
                return i

            i = i + 1

        return -1
