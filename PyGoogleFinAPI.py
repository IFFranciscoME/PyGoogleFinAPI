# -- ------------------------------------------------------------------------------ -- #
# -- Funciones de Google Finance API ---------------------------------------------- -- #
# -- Desarrollador Inicial: IF Francisco ME --------------------------------------- -- #
# -- Licencia: MIT ---------------------------------------------------------------- -- #
# -- ------------------------------------------------------------------------------ -- #

import json
from urllib2 import Request, urlopen

googleFinanceKeyToFullName = {
    u'id': u'ID',
    u't': u'StockSymbol',
    u'e': u'Index',
    u'l': u'LastTradePrice',
    u'l_cur': u'LastTradeWithCurrency',
    u'ltt': u'LastTradeTime',
    u'lt_dts': u'LastTradeDateTime',
    u'lt': u'LastTradeDateTimeLong',
    u'div': u'Dividend',
    u'yld': u'Yield',
    u's': u'LastTradeSize',
    u'c': u'Change',
    u'el': u'ExtHrsLastTradePrice',
    u'el_cur': u'ExtHrsLastTradeWithCurrency',
    u'elt': u'ExtHrsLastTradeDateTimeLong',
    u'ec': u'ExtHrsChange',
    u'ecp': u'ExtHrsChangePercent',
    u'pcls_fix': u'PreviousClosePrice'
}


def buildUrl(symbols):
    symbol_list = ','.join([symbol for symbol in symbols])
    # a deprecated but still active & correct api
    return 'http://finance.google.com/finance/info?client=ig&q=' \
           + symbol_list


def request(symbols):
    url = buildUrl(symbols)
    req = Request(url)
    resp = urlopen(req)
    # remove special symbols such as the pound symbol
    content = resp.read().decode('ascii', 'ignore').strip()
    content = content[3:]
    return content


def replaceKeys(quotes):
    global googleFinanceKeyToFullName
    quotesWithReadableKey = []
    for q in quotes:
        qReadableKey = {}
        for k in googleFinanceKeyToFullName:
            if k in q:
                qReadableKey[googleFinanceKeyToFullName[k]] = q[k]
        quotesWithReadableKey.append(qReadableKey)
    return quotesWithReadableKey


def getQuotes(symbols):
    if type(symbols) == type('str')
        symbols = [symbols]
    content = json.loads(request(symbols))
    return replaceKeys(content)


getQuotes(['AAPL', 'GOOG'])
