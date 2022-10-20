moneyStr = input("请输入金额（U/C/G）：")
while[1]:
    if moneyStr[-1] in {"U","u"}:
        U = eval(moneyStr[0:-1])*7.1915
        print("{:.2f}CNY".format(U))
        break
    elif moneyStr[-1] in {"C","c"}:
        C1 = eval(moneyStr[0:-1])/7.1915
        C2 = eval(moneyStr[0:-1])/8.01
        print("{:.2f}USD".format(C1),"{:.2f}GBP".format(C2))
        break
    elif moneyStr[-1] in {"G","g"}:
        G = eval(moneyStr[0:-1])*8.01
        print("{:.2f}CNY".format(G))
        break
    else:
        print("输入格式错误，请重新输入")
    moneyStr = input("请输入金额（U/C/G）：")
