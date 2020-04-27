# UDinformaticaProlog
Sistema de detección de mapa de contagios en prolog

# Lenguajes
 Javascript 
 
# Interfaz gráfica
- HTML
- CSS

# Herramienta Prolog:
- Tau Prolog - Versión 0.2.83

## ¿Qué es Tau Prolog?
Tau Prolog es un intérprete de Prolog implementado completamente en JavaScript. Es una implementación de Prolog guiada por el estándar ISO Prolog. Lo que distingue a Tau Prolog de otros intérpretes ejecutados en el lado del servidor, es su capacidad de integración e interacción con los elementos de las páginas web. 

### Instalación
Una vez descargado y alojado el correspondiente fichero de Tau Prolog, simplemente hay que insertarlo en la cabecera de la página web.
<script type="text/javascript" src="tau-prolog.js"></script>

También es posible descargar los ficheros fuente por separado e insertarlos individualmente en la página web. En ese caso, es importante cargar primero el núcleo de la biblioteca antes que cualquier otro módulo.

<script type="text/javascript" src="tau-prolog/core.js"></script>
<script type="text/javascript" src="tau-prolog/lists.js"></script>

...

### Sesiones
Todos los métodos de Tau Prolog están contenidos en un objeto JavaScript llamado pl, que es visible en el ámbito global.El uso de Tau Prolog está orientado a la manipulación de sesiones. Una sesión permite analizar y cargar múltiples programas y módulos, así como lanzar objetivos. Para crear una nueva sesión se provee de la función pl.create, que devuelve un objeto pl.type.Session (todos los prototipos implementados por Tau Prolog están definidos en pl.type).

  var session = pl.create();
  
Esta función acepta un parámetro opcional limit, que indica el número máximo de pasos de resolución que puede dar el intérprete para encontrar una respuesta. Esto evita que el navegador se bloquee, ya sea porque el intérprete tarde mucho en encontrar una respuesta, o porque haya entrado en una rama infinita.

### Cargar programas y módulos
Para analizar y cargar programas en una sesión, el prototipo pl.type.Session disponde del método consult, que recibe un programa en forma de cadena de caracteres y, si todo va bien, añade las reglas analizadas a la base de datos de la sesión y devuelve true.

  var parsed = session.consult("
  	:- use_module(library(lists)).
  	fruit(apple). fruit(pear). fruit(banana).
  	fruits_in(Xs, X) :- member(X, Xs), fruit(X).
  "); // true

### Errores

Los errores se devuelven en formato de término Prolog (véase [Prototipos y objetos Prolog] #Errores del manual de Tau Prolog), con información acerca de dónde se ha producido el error, esto es la línea y la columna, el token encontrado (si existe) y el siguiente carácter esperado.

### Consultas

De forma análoga a la carga de programas, para consultar objetivos en una sesión el prototipo pl.type.Session disponde del método query, que recibe un objetivo en forma de cadena de caracteres y, si todo va bien, añade el objetivo a la pila de estados de la sesión y devuelve true.

var parsed = session.query("fruits_in([carrot, apple, banana, broccoli], X)."); // true

Una vez añadido el objetivo, el método answer de pl.type.Session permite buscar las respuestas computadas. Tau Prolog es un intérprete asíncrono, por lo tanto answer no devuelve ningún resultado, sino que ejecuta una función a modo de callback. Esta asincronía permite que los predicados Prolog realicen operaciones asíncronas, como dormir la ejecución un cierto tiempo o hacer peticiones.

var callback = console.log;
session.answer( callback );

Si se encuentra una respuesta computada, esta se devuelve en un objeto del prototipo pl.type.Substitution, donde cada variable del objetivo se liga con un valor. Este prototipo implementa el método toString para obtener una representación textual de la substitución, de la forma {X/a, Y/b, Z/c, ...}

## Ejercicio Planteado

Para el ejercicio planteado se evalúa el camino de contactos que ha tenido una persona con base en unos conocimientos preestablecidos. 
al indicar el nombre de una persona, si el sistema lo encuentra en su base de conocimientos como contagiado mostrará este resultado junto con el camino de contactos que ha tenido hasta n niveles. 

