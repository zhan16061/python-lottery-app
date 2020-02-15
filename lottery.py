def getPlayerNumbers():
    userNumbers = input("輸入你要投注的號碼 6 隔，並請使用逗點分開。如 '1, 2, 3'\n：")
    userNumbersList = userNumbers.split(',')
    userNumbersSet = {int(number) for number in userNumbersList}
    return userNumbersSet

print(getPlayerNumbers())