# FSI-Searching-Algorithms
#### Algoritmos de búsqueda para hallar el camino más corto (Aquel que tiene menos coste) en el mapa de Rumanía entre dos ciudades.

Los Algoritmos de Búsqueda que se pueden encontrar son los siguientes:

**Búsqueda en Anchura**: (Ya implementado por defecto)

**Búsqueda en Profundidad**: (Ya implementado por defecto)

**Búsqueda con Branch & Bound**: 

Su implementación se basa en que a la hora de introducir los nodos en la pila, éstos se ordenan por su *path_cost*, de forma que el algoritmo tratará de coger como siguiente nodo (o ciudad) aquel que conlleve menor coste de trayecto.

**Búsqueda con Branch & Bound con Subestimación (Heurística)**: 

Su implementación se basa en una mejora del Branch & Bound original, dado a que a la hora de introducir los nodos en la pila, éstos no sólo se ordenan por su *path_cost*, sino que también lo harán por una heurística (subestimada) que se basa en la distancia en línea recta entre cada ciudad y la ciudad final/destino.

#### Resultados

Los resultados se pueden ver en el fichero *run.py* (Comentados). 

Como se puede observar, mientras que la búsqueda en anchura o búsqueda en profundidad no tienen por qué llevar a la solución más óptima (Aquel que tiene menos coste de trayecto), la búsqueda con Branch & Bound sí que asegura la optimalidad.

Además, Branch & Bound con subestimación visita menor cantidad de nodos como se puede visualizar por lo que no solo lleva a la solución más óptima, sino que lo hará con un coste computacional menor gracias a su heurística.

#### Implementación

Los ejemplos se ubican en el archivo *run.py*.

El algoritmo en el archivo *search.py*.

Las implementaciones de las distintas pilas en *utils.py*.