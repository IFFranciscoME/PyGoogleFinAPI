# -- ------------------------------------------------------------------------------ -- #
# -- Funciones de Google Finance API ---------------------------------------------- -- #
# -- Desarrollador Inicial: IF Francisco ME --------------------------------------- -- #
# -- Licencia: MIT ---------------------------------------------------------------- -- #
# -- ------------------------------------------------------------------------------ -- #

import pandas as pd
import urllib2
import datetime as dt


# ------------------------------------------------ Obtener Precios Historicos OHLCV -- #


def histprices(simbolo, periodo, ventana):
    periodo = (periodo * 60)
    url_raiz = 'http://www.google.com/finance/getprices?i='
    url_raiz += str(periodo) + '&p=' + str(ventana)
    url_raiz += 'd&f=d,o,h,l,c,v&df=cpct&q=' + simbolo
    response = urllib2.urlopen(url_raiz)
    datos = response.read().split('\n')
    datos_finales = []
    ancla = ''
    end = len(datos)
    bolsa = datos[0].split("EXCHANGE%3D")[1]
    for i in range(7, end):
        cdatos = datos[i].split(',')
        if 'a' in cdatos[0]:
            ancla = cdatos[0].replace('a', '')
        else:
            try:
                csiguiente = int(cdatos[0])
                cts = int(ancla) + (csiguiente * periodo)
                datos_finales.append((dt.datetime.fromtimestamp(float(cts)),
                                      float(cdatos[1]),
                                      float(cdatos[2]),
                                      float(cdatos[3]),
                                      float(cdatos[4]),
                                      float(cdatos[5]),
                                      bolsa))
            except: pass
    df = pd.DataFrame(datos_finales)
    df.columns = ['TimeStamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'Exchange']
    return df

Titulos = ("AC", "ALFAA", "ALSEA", "AMXL", "ASURB", "BIMBOA", "CEMEXCPO", "ELEKTRA",
            "FEMSAUBD", "GAPAB", "GCARSOA1", "GENTERA", "GFINBURO", "GFNORTEO",
            "GFREGIOO", "GMEXICOB", "GRUMAB", "ICA", "ICHB", "IENOVA", "KIMBERA",
            "KOFL", "LABB", "LACOMERUBC", "LALAB", "LIVEPOLC1", "MEXCHEM", "NEMAKA",
            "OHLMEX", "OMAB", "PE&OLES", "PINFRA", "SANMEXB", "SIMECB", "SITESL",
            "TLEVISACPO", "WALMEXV")

histprices(Titulos[4], 5, 1)