# PyGoogleFinAPI

Este repositorio forma parte del repositorio institucional de la carrera de **Ingeniería Financiera ofertada** en [ITESO](http://www.iteso.mx/), el cual puede ser consultado en la dirección [github.com/ITESOIF](https://github.com/ITESOIF).

Este código permite la conexión con [Google Finance](http://www.google.com/finance) y descargar información de instrumentos financieros, en esta versión soporta las siguientes peticiones:

- Descargar Precios Históricos

Para intervalos de tiempo desde cada minuto hasta Diarios

```python
Titulos = ("AC", "ALFAA", "ALSEA", "AMXL", "ASURB", "BIMBOA", "CEMEXCPO", "ELEKTRA",
            "FEMSAUBD", "GAPAB", "GCARSOA1", "GENTERA", "GFINBURO", "GFNORTEO",
            "GFREGIOO", "GMEXICOB", "GRUMAB", "ICA", "ICHB", "IENOVA", "KIMBERA",
            "KOFL", "LABB", "LACOMERUBC", "LALAB", "LIVEPOLC1", "MEXCHEM", "NEMAKA",
            "OHLMEX", "OMAB", "PE&OLES", "PINFRA", "SANMEXB", "SIMECB", "SITESL",
            "TLEVISACPO", "WALMEXV")

histprices(Titulos[4], 5, 1)
```
