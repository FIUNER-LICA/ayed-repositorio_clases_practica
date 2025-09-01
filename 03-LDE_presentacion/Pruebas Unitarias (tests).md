# Para ejecutar los tests provistos por la cátedra deben asegurarse de lo siguiente:

* el archivo con las pruebas debe estar dentro de la carpeta `tests` de la estructura de carpetas del repositorio
* deben completar esta linea:
``` python
from modulos import ListaDobleEnlazada
```
`modulos` hace referencia a la carpeta modulos. A eso le falta completar con el nombre del archivo que hayan elegido. La sintaxis es: `modulos.nombre_del_archivo` (sin el .py) y la clase lista doblemente enlazada debe llamarse _exactamente_ `ListaDobleEnlazada`. Entonces por ejemplo podría ser `from modules.LDE import ListaDobleEnlazada`

* les sugiero comentar todos los tests (a partir de la línea 71, a partir de las dos líneas punteadas) e ir descomentándolos de a uno, de modo de probar método por método en lugar de ejecutar todos los test de una y arriesgarse a que surjan múltiples errores y sea mas difícil de reconocer. La idea de esta sugerencia es básicamente probar los test de a uno.

* para **comentar** varias líneas de código a la vez pueden usar el atajo de teclado: ctrl (mantener) + k (presionar y soltar) + c (presionar y soltar, y soltar ctrl)
la c es por `comment`

* para **descomentar** varias lineas de código a la vez pueden usar el atajo de teclado: ctrl (mantener) + k (presionar y soltar) + u (presionar y soltar, y soltar ctrl)
la u es por `uncomment`

* finalmente, para ejecutar el test, simplemente hay que ejecutar el script (con el triangulito de ejecución de arriba a la derecha por ejemplo). Una vez ejecutado va a informar los fallos, los errores y los métodos que hayan funcionado bien.

Cuando vayan a ejecutar las pruebas unitarias, cualquier duda o dificultad que surja, me avisan y los vamos resolviendo.
💪🏼