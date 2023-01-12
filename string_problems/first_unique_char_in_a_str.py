class FirstUniqueCharacterInString:
    def firstUniqChar(self, s: str) -> int:
        char_freq_map = [0] * 26
        left = 0
        right = 0
        sLen = len(s)

        while left < sLen and right < sLen:
            key = ord(s[right]) - ord('a')
            char_freq_map[key] += 1

            while left <= right and char_freq_map[ord(s[left]) - ord('a')] > 1:
                left += 1

            right += 1

        if left >= sLen:
            return -1
        else:
            return left
