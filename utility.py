

rus_to_eng = {
    'Сделки': 'Trades',
    'Дивиденды': 'Dividends',
    'Удерживаемый налог' : 'Withholding Tax',
    'Вводы и выводы средств' : 'Deposits & Withdrawals',
    'Отчет о денежных средствах': 'Cash Report',
    'Начальная сумма средств': 'Starting Cash',
    'Конечная расчетная сумма средств': 'Ending Cash',
    'Акции - Содержится в Interactive Brokers (U.K.) Limited, обслуживается компанией Interactive Brokers LLC': 'Stocks',
    'Forex - Содержится в Interactive Brokers (U.K.) Limited, обслуживается компанией Interactive Brokers LLC': 'Forex',
    'Символ':'Symbol',
    'ID контракта':'Conid',
    'Описание':'Description',
    'Класс актива':'Asset Category',
    'Множитель':'Multiplier',
    'Информация о финансовом инструменте': 'Financial Instrument Information',
    'Количество': 'Quantity',
    'Цена транзакции': 'T. Price',
    'Комиссия/плата': 'Comm/Fee',
    'Валюта': 'Currency',
    'Отчет по базовой валюте': 'Base Currency Summary',
    'Дата расчета': 'Settle Date',
    'Валютная сводка': 'Currency Summary',
    'Всего': 'Total',
    'Сумма': 'Amount',
    'Акции': 'Stocks',
    'Дата': 'Date',
    'Дата/Время': 'Date/Time',
    'Сделки': 'Trades'
}

def process_row(row):
    for i in range(len(row)):
        if row[i] in rus_to_eng:
            row[i] = rus_to_eng[row[i]]
        else:
            row[i] = row[i].replace('Наличный дивиденд', 'Cash Dividend').replace('Всего', 'Total')