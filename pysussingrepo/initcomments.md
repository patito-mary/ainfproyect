README - 
Los codigos de esta carpeta estan hechos para manipular los catalogos de halos y merger trees. 

Hay 3 grupos de scripts incluidos aqui:

1. Codigos cuyo uso esta enfocado en manipular los forests
__Recordemos que esto de forest proviene de el uso de los merger trees de manera conjunta para mantener secuencialidad de grupo__
2. Codigo para pasar de binario a ascii (read_bin)
3. Scripts extras para comportamientos extraños o necesidades especificas

Por otro lado tenemos los codigo hechos para manipular los catalogos de Rockstar en formato sussing. Esto se puede hacer utilizando 'make' y compila todos los codigos en ./src y crea archivos del siguiente tipo:
    - `'split_forests'` : codigo que lee archivos en ascii o binario y los pasa a pequeñas cajas con distribucion secuencial tipo forest. Luego entrega el output en ascii o binario. La conversion es hecha automaticamente de acuerdo a la seleccion, este codigo tambien puede ser usado para convertir el formato de los catalogos de uno a otro
    - `'select_forests'` : codigo que se usa para generar una caja de calibracion para la simulacion. Toma los halos a z=0 y genera una lista nueva con los forests donde se encuentran dichos halos, dejando afuera a los repetidos
    - `'extract forests'` : Al igual que el anterior, codigo que sirve para generar una caja de calibracion para la simulacion. Toma la lista de forests generados anteriormente y se usa para escribir un nuevo set de catalogos pero solo incluyendo the selected forest ('select_forests'). Este codigo no necesita ser recompilado para usar en otras simulaciones
    - `'The read_bin codes'` : Tres codigos que se encuentran en la seccion de ./read_bin/ que se pueden compilar hacendo make dentro de la carpeta y que permiten leer catalogos en binario de: halos list, merger tree y forest list, analizado la version ascii en stdout. Puede usarse tambien para checkear incosistencias o recuperar los archivos originales

Aqui vienen incluidos tambien los directorios extras que procesan, analizan y hacen una serie de tareas especificas en los catalogos usando python pero no son parte de lo que normalmente se usa para los catalogos de rockstar-sussing. 
    - `'check_order.py'`: Se ordenan los halos en funcion de su posicion en la lista original. Esto se hace revisando el comportamiento de la segunda columna del archivo (de las lista de halos)
    - `'reverse_tree.py'`: Considerando los progenitores, se toma el archivo de merger trees y en formato ascii se ponen al reves, onda de progenitor a hijo. Esto se puede usar para comparar con otros merger trees y agregar un 'consistentTrees' donde se encuentren aquellos que son compatibles entre si y que incluyen Rockstar (esto e sporque existen varios mergertrees que ordenan pero dejar Rockstar al reves igual xdxdx)