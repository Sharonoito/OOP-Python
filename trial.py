from bank import MobileMoneyAccount
mm=MobileMoneyAccount(name="Sharon",phone="076565566",service_provider="Safaricom")
print(mm.deposit(1000))
print(mm.buy_airtime(100))
mm.get_statement()