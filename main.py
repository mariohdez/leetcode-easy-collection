from string_problems.longest_common_prefix import LongestCommonPrefixSolution

def main() -> int:
    strs = ["flower","flow","flight"]
    test = LongestCommonPrefixSolution()
    result = test.longestCommonPrefix(strs=strs)
    print(result)

    return 0

if __name__ == "__main__":
    main()
