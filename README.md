# Práctica final de Gestion del conocimiento y mundo empresarial

#### Alberto Martín Núñez

## Indice de contenidos

1. [Objetivo de la práctica](#id1)
2. [Recopilacion de informacion](#id2)
    1. [Método de Numbeo](#id2.1)
    2. [Método de Europa](#id2.2)
    3. [Limpieza de los datos](#id2.3)
3. [Visualización de los datos](#id3)
4. [Conclusiones](#id4)


## Objetivo de la práctica <a name="id1"></a>

El objetivo de este trabajo final de la asignatura consiste en realizar una comparacion entre dos sistemas de medicion sobre la **Calidad de vidad** en las ciudades, centrandonos en las ciudades Europeas(concretamente en 33 ciudades, que son las comunes entres los dos sistemas de medición). Esto se ha hecho así porque Numbeo si contiene datos actualizados pero los datos de Europa vienen dados por un documento que se realiza cada ciertos años y aun no ha salido el nuevo, por tanto, los datos recopilados se remontan a los de 2015. A pesar de haber transcurrido 5 años, esta informacion nos es suficiente para realizar el estudio.

Se utilizarán dos sistemas de medición diferentes:

- Por un lado de forma cuantitativa, el método de Numbeo, basado en una fórmula.
- Y por otro lado de manera cualitativa, el método de Europa, basado en una encuesta.

Por ello se estudiarán los distintos métodos asi como los ranking que se obtendrán con el fin de observar si existen diferencias a la hora de medir la **calidad de vida** de forma nuḿerica o haciendo uso de una serie de preguntas a la población(cuestionario). 

## Recopilacion de informacion <a name="id2"></a>

Aqui hablaremos de donde hemos sacado la informacion de los distintos métodos.

## Método de Numbeo <a name="id2.1"></a>

Numbeo es una base de datos global de múltiples fuentes de información sobre la calidad de vida en donde existen diversos indicadores como *tasas de criminilidad*, *calidad de atencion médica*. 

Numbeo nos proporciona una herramienta para poder ver, compartir y comparar sobre la calidad de vida en las ciudades. La calidad de vida para Numbeo se basa en los siguientes datos:

- Costo de vida
- Asequibilidad de la vivienda
- Contaminacion(aire,agua,etc)
- Tasas de crimen
- Calidad del sistema de salud
- Tráfico(tiempos de viaje)

Con estos datos se crea una fórmula la cual es utilizada para sacar un valor para cada ciudad y de esta forma tener un ranking como el siguiente:

![Current Quality of Life Index by City 2020](./img/ranking_2020.jpeg)



Como se ha mencionado al principio, se ha escogido el ranking del año 2015 para poder comparar con el siguiente método a explicar.
 
## Método de Europa <a name="id2.2"></a>

Este Flash Eurobarameter, “Calidad de vida en las ciudades europeas” (n. ° 419), se realizó por medio de la Dirección General de Política Regional y Urbana con el objetivo de obtener una instantánea de opiniones de las personas sobre una serie de cuestiones urbanas. 

La encuesta se realizó en un total de 83 ciudades europeas. En cada ciudad se entrevistó a unos 500 ciudadanos, en total unos 40.798 encuestados de diferentes grupos demográficos.

En el propio documento que se ha extraído con toda la informacion del *Flash Eurobarameter* se encuentran cada una de las preguntas que se realizaron y el porcentaje de las personas que estaban "de media" satisfechas con cada pregunta realizada.

Aqui tenemos un ejemplo con el resultado a la pregunta **"Your personal job situation"**:

![Cuestion Personal Job situation](./img/example_personal_job.jpeg)

El problema con estos datos es que no existé un ranking para poder ver de una forma más clara que ciudades son las que tienen mayor calidad de vida. Por lo que tuve que coger todos los resultados de cada pregunta(porcentajes) para cada ciudad y hacer una media y por así obtener un ranking propio. Este resultado residen en un excel bastanta grande como para ponerlo aqui, por eso, simplemente añado la tabla que ahce referencia al ranking de las 83 ciudades en donde se realizo la encuesta de Europa.

| Nº |       Ciudad       | Porcentaje 2015 |
|:--:|:------------------:|:---------------:|
|  1 |       Zurich       |       85%       |
|  2 |       Aalborg      |       81%       |
|  3 |      Groningen     |       81%       |
|  4 |     Luxembourg     |       81%       |
|  5 |       Rennes       |       79%       |
|  6 |        Wien        |       79%       |
|  7 |        Oslo        |       79%       |
|  8 |      Helsinki      |       79%       |
|  9 |       Munchen      |       78%       |
| 10 |        Oulu        |       78%       |
| 11 |        Graz        |       78%       |
| 12 |       Cardiff      |       78%       |
| 13 |       Belfast      |       78%       |
| 14 |      Stockholm     |       77%       |
| 15 |       Glasgow      |       77%       |
| 16 |      Newcastle     |       77%       |
| 17 |      Antwerpen     |       77%       |
| 18 |      Bordeaux      |       76%       |
| 19 |       Geneva       |       76%       |
| 20 |      Kobenhavn     |       76%       |
| 21 |        Malmo       |       75%       |
| 22 |      Bialystok     |       75%       |
| 23 |     Strasbourg     |       75%       |
| 24 |       Oviedo       |       75%       |
| 25 |       Hamburg      |       75%       |
| 26 | Greater_Manchester |       74%       |
| 27 |       Rostock      |       74%       |
| 28 |      Rotterdam     |       74%       |
| 29 |       Leipzig      |       74%       |
| 30 |     Manchester     |       74%       |
| 31 |        Braga       |       74%       |
| 32 |      Amsterdam     |       73%       |
| 33 |      Ljubljana     |       73%       |
| 34 |       Dublin       |       72%       |
| 35 |      Reykjavik     |       72%       |
| 36 |       London       |       72%       |
| 37 |     Cluj_Napoca    |       72%       |
| 38 |       Gdansk       |       72%       |
| 39 |      Dortmund      |       71%       |
| 40 |       Zagreb       |       71%       |
| 41 |    Piatra_Neamt    |       69%       |
| 42 |        Essen       |       69%       |
| 43 |       Vilnius      |       69%       |
| 44 |       Burgas       |       69%       |
| 45 |        Praha       |       69%       |
| 46 |        Lille       |       68%       |
| 47 |       Tallinn      |       68%       |
| 48 |       Antalya      |       68%       |
| 49 |       Krakow       |       68%       |
| 50 |       Malaga       |       67%       |
| 51 |       Berlin       |       67%       |
| 52 |       Ostrava      |       67%       |
| 53 |       Verona       |       67%       |
| 54 |        Paris       |       67%       |
| 55 |  Brussel/Bruxelles |       67%       |
| 56 |    Greater_Paris   |       66%       |
| 57 |      Barcelona     |       65%       |
| 58 |      Warszawa      |       65%       |
| 59 |     Diyarbakir     |       65%       |
| 60 |        Liege       |       65%       |
| 61 |        Riga        |       65%       |
| 62 |       Kosice       |       64%       |
| 63 |   Greater_Lisbon   |       63%       |
| 64 |       Bologna      |       63%       |
| 65 |       Ankara       |       62%       |
| 66 |      Budapest      |       62%       |
| 67 |      Lefkosia      |       61%       |
| 68 |      Marseille     |       60%       |
| 69 |       Miskolc      |       60%       |
| 70 |       Torino       |       59%       |
| 71 |      Valletta      |       59%       |
| 72 |       Lisboa       |       58%       |
| 73 |       Madrid       |       58%       |
| 74 |     Bratislava     |       57%       |
| 75 |      Irakleio      |       56%       |
| 76 |        Sofia       |       54%       |
| 77 |      Bucuresti     |       54%       |
| 78 |      Istanbul      |       52%       |
| 79 |       Napoli       |       49%       |
| 80 |   Greater_Athens   |       48%       |
| 81 |        Roma        |       48%       |
| 82 |       Palermo      |       45%       |
| 83 |       Athina       |       44%       |


## Limpieza de los datos <a name="id2.3"></a>

