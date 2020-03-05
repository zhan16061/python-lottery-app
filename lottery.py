import random

def menu():
    userNumbers = getPlayerNumbers()
    lotteryNumbers = createLotteryNumbers()
    matchNumbers = userNumbers.intersection(lotteryNumbers)
    print('中獎號碼為{}, 中獎金額為{}'.format(matchNumbers, 1000 * len(matchNumbers)))

def getPlayerNumbers():
    userNumbers = input("輸入你要投注的號碼 6 隔，並請使用逗點分開。如 '1,2,3,4,5,6'\n：")
    userNumbersList = userNumbers.split(',')
    userNumbersSet = {int(number) for number in userNumbersList}
    return userNumbersSet


def createLotteryNumbers():
    numberSet = set()  # 初始化 set，請勿使用 {}
    while len(numberSet) < 6:
        numberSet.add(random.randint(1, 10))
    return numberSet


# print('你輸入的號碼為：{playerNumbers}'.format(playerNumbers=getPlayerNumbers()))
# print('樂透號碼為：{lotteryNumbers}'.format(lotteryNumbers=createLotteryNumbers()))
menu()