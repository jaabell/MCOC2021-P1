# MCOC2021-P1
Optimización estructural de un puente reticular


## Cual fue su diseño inicial?
R: El diseño inicial, consistia en un enrejado tipo Pratt invertido, restrigiendo todos los GDL mediante barras cruzadas,
utilizando la sección tipo cajon mas grande posible


## Cuanto pesaba?
R: 800 toneladas aproximadamente


## Como eran los factores de utilización y deformaciones?
R: Eran bastante bajos, la barra mas utilizada, quer eran las laterales del tablero, tenian un factor de 0.1.
Las deformaciones eran bastante bajas por la sobre-deformación.


## 
Al principio el peso del puente era de aproximadamente 800 toneladas. En este punto se estaban utilizando 2 secciones para las barras del puente.
Luego, se agrego una seccion mediana y se fue iterando los tipos de secciones probando distintas secciones, pesos y dimensiones, la cual permitio bajar el peso del puente hasta 400 toneladas.
Al ver que el peso no variaba mucho mas a medida que variaban las secciones se decidio incluir otra seccion pequeña, que fuera mayor a la mas chica pero que a la ver fuera menor a la mediana. En esta seccion se fue iterando las dimensiones, peso y tipo hasta encontrar un optimo, el cual era de 200 toneladas.
Finalmente se agrego una quinta seccion que se encontraba entre la seccion mediana y la mas grande, iterando esta seccion se obtuvo que el peso del reticulado disminuyo a casi 95 toneladas, es decir disminuyo casi 10 veces el peso del puente.
Para decidir que barras del puente debian cambiar sus secciones se utilizaron los factores de utilizacion, si las barras tenian un factor de utilizacion muy pequeño se disminuia su seccion, en cambio si la el factor de utilizacion era muy grande, la seccion de esas barras debia aumentar. Por medio de esto tambien se vio que habian barras que no estaban siendo utilizadas, por lo que se eliminaron esas barras.
Luego de eliminar las barras sobrantes se llego a que el peso del puente era de 85 toneladas aproximadamente. Finalmente, se cambiaron las secciones de las barras diagonales por unas de seccion circular. Con este cambio el peso final del puente quedo en 82 toneladas aproximadamente. Las secciones de las barras con que se obtuvo este peso son:
 * H900x300x143.5
 * H900x300x134.4
 * H800x300x126.5
 * H450x150x35.9
 * []12x12x0.3
 * O210x200
 * o12.7x10.9

