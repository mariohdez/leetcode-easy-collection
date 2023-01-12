from array_problems.max_profit import MaxProfitSolution

def main() -> int:
    prices = [7,1,5,3,6,4]
    test = MaxProfitSolution()
    result = test.maxProfit(prices)
    print(result)

    return 0

if __name__ == "__main__":
    main()
