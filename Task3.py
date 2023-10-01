# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01
operations_info = list()

def add_bank(cash: float) -> None:
    global bank
    global count
    global operations_info
    bank += cash
    count += 1
    operations_info.append(cash)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    global operations_info
    bank -= cash
    count += 1
    operations_info.append(-cash)
    if cash*percent_take < 30:
        bank -= 30
        print("Списаны проценты за снятие:", 30)
    elif cash*percent_take > 600:
        bank -= 600
        print("Списаны проценты за снятие:", 600)
    else:
        bank -= cash * percent_take
        print("Списаны проценты за снятие:", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере:", round((percent_add * bank), 2))


def exit_bank():
    print("Рады вас видетеь снова!")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50: "))
        if cash % 50 == 0:
            return cash
        else:
            print('Некорректный ввод')

def rich_nalog() -> float:
    global bank
    global percent_tax
    if bank > 5_000_000:
        bank = bank - bank * percent_tax
        print("Cписан налог на богатство: ", round((bank * percent_tax), 2))

def operation_info() -> None:
    global operations_info
    for cash in operations_info:
        if cash > 0:
            print(f'Зачисление: {cash}')
        else:
            print(f'Снятие: {-cash}')

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - информация об операциях\n5 - выйти\nВаш выбор: ")

    if action == '1':
        print('Вы выбрали "снять деньги"')
        rich_nalog()
        cash = check_bank()
        if cash < bank:
            take_bank(cash)
        else:
            print("Недостаточно средств")
        rich_nalog()
    elif action == '2':
        print('Вы выбрали "пополнить баланс"')
        add_bank(check_bank())
        rich_nalog()
    elif action == '3':
        print("Баланс =", round(bank, 2))
    elif action == '5':
        exit_bank()
    elif action == '4':
        print('Вы выбрали "информация об операциях"')
        operation_info()
    else:
        print('Неверный ввод\n')
