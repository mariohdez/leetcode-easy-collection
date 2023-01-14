from typing import List
class LongestCommonPrefixSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""

        strToLenMap = {}
        guidingStr = strs[0]
        i = 0
        commonPrefix = ""

        for str in strs:
            strToLenMap[str] = len(str)

        while i < strToLenMap[guidingStr]:
            for j in range(1, len(strs)):
                if i >= strToLenMap[strs[j]] or guidingStr[i] != strs[j][i]:
                    return commonPrefix

            commonPrefix += guidingStr[i]
            i = i + 1

        return commonPrefix
