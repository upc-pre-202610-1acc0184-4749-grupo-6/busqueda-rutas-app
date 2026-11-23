# GUIÓN OFICIAL DE EXPOSICIÓN ORAL — SEGUNDO HITO (TB2)
## Resolución y Validación del Sudoku Generalizado $N \times N$ mediante Grafos de Restricciones y Búsqueda Informada

**Institución:** Universidad Peruana de Ciencias Aplicadas (UPC)  
**Curso:** Complejidad Algorítmica (1ACC0184) — Sección 4749  
**Docente:** Prof. José Luis Soncco Alvarez  
**Grupo:** N.° 5  
**Tiempo Límite:** 10 a 12 minutos (Estricto según rúbrica)  
**Código de Vestimenta:** Formal ejecutiva  

---

### TABLA RESUMEN DE ROLES, TIEMPOS Y DIAPOSITIVAS

| Bloque | Ponente | Código | Diapositivas | Rol Técnico y Temas Clave | Tiempo Estimado |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Bloque 1** | **Kobashigawa** | u202412921 | Diapositivas 1 a 4 | Portada, Problemática en la Industria, NP-Completitud (Yato & Seta) y Grafo de 2,401 nodos | 00:00 – 03:30 (3.5 min) |
| **Bloque 2** | **Pareja** | u202411627 | Diapositivas 5 a 8 | Propuesta en 3 Niveles, Heurística MRV (Fail-First), Bitmasks $O(1)$ con POPCNT y Análisis Big-O | 03:30 – 07:00 (3.5 min) |
| **Bloque 3** | **Riveros** | u20241c998 | Diapositivas 9 a 13 | Arquitectura MVC / UML, Demostración GUI Tkinter, Benchmarking (21 Pistas), Conclusiones y Cierre | 07:00 – 11:00 (4.0 min) |
| **Defensa** | **Equipo Completo (Grupo 5)** | Todos | Diapositiva 13 | Ronda de Preguntas Técnicas Individuales del Docente | 11:00 – 15:00 (~4 min) |

---

## BLOQUE 1: FUNDAMENTACIÓN TEÓRICA, CONTEXTO Y MODELADO TOPOLÓGICO
**Ponente:** Kobashigawa (u202412921)  
**Tiempo Asignado:** 3 minutos y 30 segundos  
**Diapositivas:** 1 a 4  

---

### [DIAPOSITIVA 1: PORTADA OFICIAL]
*(Tiempo: 00:00 - 00:35)*  
*(Indicación: Postura erguida, contacto visual directo con el profesor Soncco y la cámara/jurado. Tono seguro, profesional y pausado).*

**Kobashigawa:**  
> "Buenos días, estimado profesor José Luis Soncco y compañeros presentes.  
> 
> A nombre del Grupo 5, conformado por Pareja, Riveros y mi persona, Kobashigawa, estudiantes de la carrera de Ingeniería de Software de la UPC, tenemos el agrado de presentar la sustentación del Segundo Hito (TB2) de nuestro proyecto de investigación aplicada en el curso de Complejidad Algorítmica.  
> 
> Nuestro proyecto se titula: **'Resolución y Validación del Sudoku Generalizado $N \times N$ mediante Grafos de Restricciones y Búsqueda Informada'**.  
> 
> A lo largo de esta exposición, explicaremos cómo hemos formalizado el Sudoku como un Problema de Satisfacción de Restricciones sobre una red de grafos de escala masiva, demostraremos la convergencia asintótica de la heurística informada MRV y presentaremos nuestra implementación acelerada por microcódigo de CPU, validada empíricamente en un aplicativo modular interactivo."

---

### [DIAPOSITIVA 2: CONTEXTO Y PROBLEMÁTICA]
*(Tiempo: 00:35 - 01:25)*  
*(Indicación: Cambiar a Diapositiva 2. Señalar con el puntero la métrica $10^{4058}$).*

**Kobashigawa:**  
> "Iniciamos contextualizando la relevancia del problema.  
> 
> En la industria del software y el entretenimiento interactivo inteligente —como plataformas de videojuegos cognitivos del calibre de Nintendo Brain Age o las publicaciones de Nikoli— la generación y validación inmediata de tableros lógicos es un componente crítico.  
> 
> En la cuadrícula clásica de $9 \times 9$, el espacio de tableros válidos es de aproximadamente $6.67 \times 10^{21}$, el cual puede ser explorado de forma aceptable mediante técnicas convencionales. Sin embargo, en la ingeniería del software moderna nos enfrentamos a la **formulación generalizada $N \times N$**, donde la dimensión crece como $N = k^2$. Al escalar a cuadrículas de orden superior —como $16 \times 16$ para $k=4$, o $49 \times 49$ para $k=7$— los métodos ingenuos basados en matrices planas colapsan de manera absoluta.  
> 
> Como observamos en pantalla, un algoritmo de fuerza bruta sin poda posee una cota asintótica de $O(N^{N^2})$. Para $k=7$, la cantidad de combinaciones potenciales asciende a $49^{2401}$, lo que equivale aproximadamente a **$10^{4058}$ estados**. Esta cifra supera por miles de órdenes de magnitud la cantidad total de átomos en el universo observable.  
> 
> En entornos cloud de alta concurrencia, ejecutar validadores ineficientes genera un agotamiento catastrófico de CPU y memoria. Por tanto, el reto computacional radica en modelar las restricciones mediante una topología matemática de grafos que permita habilitar podas tempranas y reducir el espacio de búsqueda a milisegundos."

---

### [DIAPOSITIVA 3: FUNDAMENTACIÓN TEÓRICA Y NP-COMPLETITUD]
*(Tiempo: 01:25 - 02:20)*  
*(Indicación: Cambiar a Diapositiva 3. Mantener un tono riguroso al citar la literatura científica).*

**Kobashigawa:**  
> "Para fundamentar teóricamente esta problemática, nos remitimos al hito matemático establecido por **Yato y Seta en 2003**, quienes demostraron formalmente que determinar si una cuadrícula de Sudoku generalizado admite una solución válida pertenece a la clase de complejidad **NP-Completo**.  
> 
> Su demostración se basa en una reducción polinomial estricta desde el problema clásico de **Coloración de Vértices en Grafos (Graph Vertex Coloring)**:
> 1. Cada celda vacía del tablero corresponde a un **vértice $v$** dentro del conjunto $V$.
> 2. El conjunto de valores admisibles del $1$ al $N$ constituye la paleta de **colores $C$**.
> 3. Y las reglas de no repetición en filas, columnas y subcuadrículas se modelan como **aristas no dirigidas $E$**, que imponen una restricción de diferencia mutua estricta entre nodos adyacentes.  
> 
> Dado que la clase NP-completa implica que no existe a la fecha un algoritmo polinomial determinista en $P$, la eficiencia de un motor de resolución depende exclusivamente de la calidad de sus **heurísticas de poda y estructuras de datos**.  
> 
> En base a esto, definimos cuatro objetivos concretos:
> - **Primero:** Modelar formalmente una red topológica masiva que supere holgadamente el requisito de 1,500 nodos de la rúbrica.
> - **Segundo:** Generar un dataset sintético reproducible y particionado equitativamente.
> - **Tercero:** Implementar un motor híbrido con heurística MRV y aceleración a nivel de bits en $O(1)$.
> - **Y cuarto:** Desarrollar un aplicativo interactivo con arquitectura MVC y telemetría en tiempo real."

---

### [DIAPOSITIVA 4: DATASET Y MODELADO TOPOLÓGICO]
*(Tiempo: 02:20 - 03:30)*  
*(Indicación: Cambiar a Diapositiva 4. Señalar la fórmula del Lema del Apretón de Manos y el gráfico de la derecha).*

**Kobashigawa:**  
> "Para materializar este marco, construimos un grafo de restricciones a escala masiva seleccionando la dimensión $k = 7$, correspondiente a un tablero de $N = 49 \times 49$.  
> 
> Como observan en la tarjeta izquierda:
> - El número total de vértices es $|V| = N^2 = 49^2 = \mathbf{2,401\text{ nodos}}$, superando ampliamente el piso de 1,500 nodos exigido en la rúbrica del curso.
> - Cumpliendo con el requerimiento de balance individual de al menos 500 nodos por integrante, particionamos el dataset de manera trazable:
>   - Mi cuota asignada comprendió **800 nodos** (Filas 0 a 15),
>   - Pareja cubrió **801 nodos** (Filas 16 a 32),
>   - Y Riveros cubrió **800 nodos** (Filas 32 a 48).  
> 
> A nivel estructural, este grafo es **regular**, lo que significa que cada vértice posee exactamente el mismo grado $d(v)$. Aplicando el principio de inclusión-exclusión:  
> $d(v) = (N - 1) + (N - 1) + (k - 1)^2 = 3N - 2k - 1$  
> Sustituyendo para $k = 7$ y $N = 49$, obtenemos que cada celda está conectada con exactamente **132 vecinos**.  
> 
> Aplicando el fundamental **Lema del Apretón de Manos (Handshaking Lemma)** de la teoría de grafos, calculamos la cardinalidad exacta de aristas:  
> $|E| = \frac{|V| \times d(v)}{2} = \frac{2,401 \times 132}{2} = \mathbf{158,466\text{ aristas}}$.  
> 
> En la Figura 1 a la derecha, apreciamos la renderización que realizamos en NetworkX y Matplotlib: a la izquierda, la red completa con su densidad característica; y a la derecha, el subgrafo inducido que evidencia la presencia de cliques completos $K_{49}$ en filas y columnas. Todo este modelo fue exportado en los archivos normalizados `sudoku_nodes.csv` y `sudoku_edges.csv`.  
> 
> Para explicar la formulación matemática de los algoritmos de resolución y la aceleración a nivel de registros de procesador, cedo la palabra a mi compañero Pareja."

---

## BLOQUE 2: PROPUESTA ALGORÍTMICA, HEURÍSTICA MRV, BITMASKS Y ANÁLISIS BIG-O
**Ponente:** Pareja (u202411627)  
**Tiempo Asignado:** 3 minutos y 30 segundos  
**Diapositivas:** 5 a 8  

---

### [DIAPOSITIVA 5: PROPUESTA ALGORÍTMICA EN 3 NIVELES]
*(Tiempo: 03:30 - 04:15)*  
*(Indicación: Cambiar a Diapositiva 5. Saludar brevemente y señalar las tres columnas progresivas).*

**Pareja:**  
> "Muchas gracias, Kobashigawa. Buenos días, profesor Soncco.  
> 
> Siguiendo con la exposición, para abordar la resolución computacional del problema diseñamos e implementamos una estrategia progresiva estructurada en **tres niveles algorítmicos**, permitiendo aislar empíricamente el impacto de cada optimización:  
> 
> - **Nivel 1 — Backtracking Básico (DFS Secuencial):** Representa nuestra línea base convencional. Explora las celdas vacías en orden secuencial fijo de izquierda a derecha. Cada intento valida restricciones mediante bucles iterativos que recorren filas, columnas y cuadrículas en tiempo $O(N)$. Carece por completo de inteligencia predictiva, explorando ramas enteras que están condenadas al fracaso. En nuestras pruebas demandó más de 38 segundos y casi 1.9 millones de retrocesos.  
> 
> - **Nivel 2 — Backtracking con Heurística MRV:** Incorpora el principio de inteligencia artificial formulado por Russell y Norvig. Selecciona dinámicamente la celda que tiene la menor cantidad de valores legales remanentes. Como veremos a continuación, esta heurística genera una **poda combinatoria del 99.23%**, colapsando los retrocesos a tan solo 14,672.  
> 
> - **Nivel 3 — MRV Optimizado con Máscaras de Bits (Bitmasks):** Mantiene con exactitud matemática el mismo árbol de decisiones del Nivel 2, pero reemplaza la gestión de conjuntos en memoria por **vectores de bits y operaciones lógicas a nivel de registros de la CPU**. Esto permite ejecutar las comprobaciones y el conteo en tiempo estricto $O(1)$, logrando un tiempo récord de **147.44 milisegundos**, lo que representa un factor de aceleración global de **258.2 veces** respecto a la línea base."

---

### [DIAPOSITIVA 6: HEURÍSTICA MRV Y PRINCIPIO FAIL-FIRST]
*(Tiempo: 04:15 - 05:05)*  
*(Indicación: Cambiar a Diapositiva 6. Enfatizar la fórmula matemática de la izquierda).*

**Pareja:**  
> "Profundicemos en el fundamento matemático de la Heurística **MRV (Minimum Remaining Values)**, también conocida como la heurística de la 'Variable Más Restringida'.  
> 
> En cada paso de la recursión, en lugar de tomar la siguiente celda vacía según el orden de lectura, el algoritmo calcula el dominio de valores admisibles $D(v)$ para todas las celdas vacías y selecciona la variable óptima $v^*$ que minimiza dicho tamaño:  
> 
> $$v^* = \arg\min_{v \in V_{\text{vacíos}}} |D(v)|$$  
> 
> Esta estrategia obedece al principio heurístico de **'Fallar Primero' (Fail-First Principle)**:  
> Si una celda tiene un dominio unitario ($|D(v)| = 1$), se asigna de forma determinista inmediata sin conjeturas. Y lo más crucial: si durante la búsqueda alguna celda agota todas sus opciones legales ($|D(v)| = 0$), el algoritmo identifica instantáneamente una inconsistencia lógica y activa un **retroceso inmediato (Dead-end pruning)**.  
> 
> En un backtracking tradicional, el algoritmo podría tardar cientos de miles de iteraciones en percatarse de que una asignación temprana dejó vacía una celda lejana. MRV lo detecta al instante, cortando de raíz subárboles enteros de tamaño $O(N^{m-1})$.  
> 
> Es vital recalcar que MRV es un algoritmo **completo y exacto**: no omite ninguna solución válida, sino que poda exclusivamente ramas que son matemáticamente inviables. Esto hace que el factor de ramificación efectivo del árbol colapse de $B \approx 9$ a tan solo $B_{\text{eff}} \approx 1.2$."

---

### [DIAPOSITIVA 7: OPTIMIZACIÓN A BAJO NIVEL: BITMASKS Y POPCNT]
*(Tiempo: 05:05 - 06:00)*  
*(Indicación: Cambiar a Diapositiva 7. Explicar con entusiasmo el código binario y la instrucción POPCNT).*

**Pareja:**  
> "Si bien el Nivel 2 redujo drásticamente el espacio de búsqueda, el cálculo repetitivo de intersecciones de conjuntos generaba un cuello de botella por la constante oculta. Para erradicarlo, en el **Nivel 3** implementamos una aceleración directa por hardware mediante **Máscaras de Bits (Bitmasks)**.  
> 
> En lugar de manipular arreglos o `sets`, representamos el estado de restricciones en tres arreglos de enteros de $N$ bits: `row_masks`, `col_masks` y `box_masks`.  
> Cuando un dígito $v$ está presente en una región, el bit en la posición $v$ se encuentra encendido en $1$.  
> 
> Gracias a la lógica booleana, verificar qué números están restringidos para una celda $(r, c)$ se resuelve mediante una simple operación **OR bit a bit** ejecutada en un único ciclo de microprocesador:  
> `usados = row_masks[r] | col_masks[c] | box_masks[b]`  
> 
> Y los dígitos legalmente disponibles se obtienen invirtiendo la máscara con una operación **NOT y AND**:  
> `disponibles = all_mask & (~usados)`  
> 
> Pero la optimización cúspide radica en cómo determinamos el tamaño del dominio $|D(v)|$. En Python 3.12, utilizamos el método nativo `int.bit_count()`. En tiempo de ejecución, el compilador traduce directamente esta función a la instrucción ensamblador **POPCNT (Population Count)**, presente en las arquitecturas modernas x86-64 y ARM.  
> 
> POPCNT cuenta cuántos bits en '1' contiene un registro en **1 solo ciclo de reloj de hardware**, reduciendo la constante asintótica de chequeo de $O(N)$ a un estricto $O(1)$.  
> 
> Como vemos en pantalla, esto produce la misma secuencia exacta de 14,672 decisiones que el Nivel 2, pero reduce el tiempo de ejecución de 3.5 segundos a **147 milisegundos**, logrando una aceleración pura de **24.2 veces** sobre MRV tradicional."

---

### [DIAPOSITIVA 8: ANÁLISIS ASINTÓTICO DE COMPLEJIDAD BIG-O]
*(Tiempo: 06:00 - 07:00)*  
*(Indicación: Cambiar a Diapositiva 8. Contrastar rigurosamente la tabla de complejidades temporales y espaciales).*

**Pareja:**  
> "Aterricemos esto en el análisis asintótico formal de complejidad Big-O, tanto temporal como espacial.  
> 
> **En Complejidad Temporal:**
> - El método exhaustivo sin poda posee una cota intratable de $O(N^{N^2})$.
> - Para el **Nivel 1**, en el peor de los casos, la cota temporal es $T_{\text{básico}}(N) = O(N \cdot N^m) = O(N^{m+1})$, donde $m$ representa el número de celdas vacías (con $m \le N^2$). Cada nodo gasta $O(N)$ verificando restricciones por bucles.
> - Para el **Nivel 2**, la complejidad se reduce a $T_{\text{mrv}}(N) = O(m \cdot N) + O(B_{\text{eff}}^d)$. Aunque evaluar dominios cuesta $O(m \cdot N)$ por nodo, el árbol explota con un factor efectivo $B_{\text{eff}} \approx 1.2$, mucho menor que $N$.
> - En el **Nivel 3**, el costo de evaluar dominios desciende a $O(m \cdot 1)$ gracias a POPCNT, manteniendo el árbol mínimo y acelerando la constante de forma masiva.  
> 
> **En Complejidad Espacial:**
> - Evaluamos la decisión estructural entre Matriz de Adyacencia y Listas de Adyacencia:  
>   Una Matriz de Adyacencia para nuestro grafo de 2,401 nodos requeriría $|V|^2 = 2401^2 \approx 5.76\text{ millones de celdas}$. Dado que la densidad del grafo es de apenas 5.5%, esto implicaría un desperdicio del 94.5% de memoria en ceros.  
>   Por ello, implementamos **Listas de Adyacencia sobre tablas hash (`set`)**, con un costo espacial óptimo de $O(|V| + |E|) \approx 160,867\text{ entradas}$, ocupando apenas **1.25 MB de memoria RAM**.
> - Sumando la pila de llamadas del sistema (call stack), cuya profundidad máxima nunca excede la cantidad de celdas vacías ($D_{\text{max}} \le N^2$), la memoria total del solver se acota estrictamente en $S(N) = O(N^2)$, garantizando estabilidad absoluta y cero riesgo de desbordamiento de pila.  
> 
> Para exponer la arquitectura de software, la demostración de la interfaz gráfica y la validación experimental, cedo la palabra a mi compañera Riveros."

---

## BLOQUE 3: ARQUITECTURA SOFTWARE, INTERFAZ GRÁFICA, BENCHMARKING Y CONCLUSIONES
**Ponente:** Riveros (u20241c998)  
**Tiempo Asignado:** 4 minutos  
**Diapositivas:** 9 a 13  

---

### [DIAPOSITIVA 9: ARQUITECTURA DE SOFTWARE Y MODELADO UML]
*(Tiempo: 07:00 - 07:50)*  
*(Indicación: Cambiar a Diapositiva 9. Saludar al profesor y explicar el diagrama de clases UML).*

**Riveros:**  
> "Muchas gracias, Pareja. Buenos días profesor Soncco y compañeros.  
> 
> Para asegurar que este motor algorítmico fuera escalable, mantenible y robusto, diseñamos la solución siguiendo principios de Ingeniería de Software bajo el patrón arquitectónico desacoplado **Modelo-Vista-Controlador (MVC)**, cumpliendo con los estándares internacionales IEEE 830 e ISO 29148.  
> 
> En el Diagrama de Clases UML que observamos a la derecha:
> - **Capa Modelo (`src/model.py`):** Define las clases nucleares `ConstraintGraph` y `SudokuBoard`. `ConstraintGraph` gestiona la topología de la red, sus listas de adyacencia y el cálculo de grados. `SudokuBoard` administra el estado matricial, las pistas fijas y la validación de colisiones. Nótese la relación fundamental de **agregación** entre ambas clases: un único grafo de restricciones permanece residente en memoria y puede ser compartido por múltiples tableros sin necesidad de recalcular aristas.
> - **Capa Controlador (`src/solver.py`):** Implementa el patrón fachada mediante la clase `SudokuSolver`, encapsulando los tres métodos de resolución (`solve_backtracking`, `solve_mrv` y `solve_bitmask`) junto con la telemetría métrica de nodos explorados y tiempo transcurrido.
> - **Capa Vista (`src/main.py`):** Construida con la librería gráfica Tkinter, encapsula la clase `SudokuApp`, gobernando la interfaz visual interactiva, eventos de teclado y renderizado dinámico.  
> 
> La arquitectura garantiza 7 Requerimientos Funcionales y 4 Requerimientos No Funcionales, tales como latencias de verificación inferiores a 100 ms y renderizado fluido a 60 cuadros por segundo."

---

### [DIAPOSITIVA 10: INTERFAZ GRÁFICA Y CASOS DE USO]
*(Tiempo: 07:50 - 08:45)*  
*(Indicación: Cambiar a Diapositiva 10. Señalar las capturas reales de la GUI en pantalla).*

**Riveros:**  
> "Pasamos a describir el comportamiento operativo de la interfaz gráfica a través de sus casos de uso clave, cuyas capturas reales apreciamos en pantalla:  
> 
> - **CU-01 — Juego Manual y Verificación de Reglas:**  
>   El usuario puede ingresar valores numéricos manualmente en el lienzo interactivo. Al pulsar el botón 'Comprobar Solución', el sistema invoca el método `conflicts()` de la capa modelo. Si existen infracciones a las reglas del grafo, las celdas en conflicto se iluminan de inmediato en un color rojo bermellón (`#D0021B`), garantizando retroalimentación visual instantánea.  
> 
> - **CU-02 — Resolución Asistida y Telemetría en Vivo:**  
>   El usuario puede seleccionar en cualquier momento el algoritmo deseado desde un menú desplegable y presionar 'Resolver con Algoritmo'. El aplicativo resuelve el puzzle, colorea las celdas calculadas en azul marino institucional (`#003366`) para distinguirlas de las pistas iniciales en negro, y actualiza de inmediato el panel inferior de telemetría con el tiempo exacto en milisegundos, el número de celdas visitadas y los retrocesos efectuados.  
>   Un detalle clave de diseño es la **persistencia y restauración automática**: si el usuario cambia de algoritmo en el combobox, el software restaura al instante las pistas originales de la partida, garantizando una comparación experimental rigurosa y equitativa sobre el mismo tablero.  
> 
> - **CU-03 — Soporte Multi-Escala Dinámico:**  
>   Como se aprecia en las capturas superior derecha e inferior, el aplicativo no está acoplado al tamaño estándar de 9×9. Cuenta con renderizado reactivo paramétrico que permite instanciar y jugar fluidamente en tableros de **4×4** ($k=2$), **9×9** ($k=3$) y hasta **16×16** ($k=4$, con 256 celdas), recalculando su geometría de manera completamente transparente."

---

### [DIAPOSITIVA 11: VALIDACIÓN EXPERIMENTAL Y BENCHMARKING]
*(Tiempo: 08:45 - 09:45)*  
*(Indicación: Cambiar a Diapositiva 11. Explicar los datos de la Tabla 1 con énfasis en las métricas).*

**Riveros:**  
> "En esta diapositiva presentamos la evidencia experimental cuantitativa que valida las afirmaciones teóricas de nuestro informe.  
> 
> Sometimos los tres niveles algorítmicos a una prueba de estrés idéntica sobre una instancia de **alta dificultad de 21 pistas iniciales** (es decir, con 60 celdas vacías por resolver). La ejecución se realizó en un entorno controlado con procesador x86-64 y Python 3.12.  
> 
> Analicemos la **Tabla 1**:  
> 1. El **Nivel 1 (Backtracking Básico)** demandó **38,074.28 milisegundos** —es decir, más de 38 segundos— requiriendo **1,897,847 nodos y retrocesos**. Esto demuestra la inviabilidad práctica de la búsqueda ciega frente a combinaciones complejas.  
> 2. Al aplicar el **Nivel 2 (Heurística MRV)**, el número de retrocesos colapsó a exactamente **14,672**. Esto representa una **reducción del 99.23% en el espacio de búsqueda inútil**, bajando el tiempo a 3,571 milisegundos.  
> 3. Finalmente, el **Nivel 3 (MRV + Bitmasks)** ejecutó exactamente los mismos **14,672 retrocesos** —lo que comprueba matemáticamente la identidad lógica de ambos algoritmos—, pero gracias a las operaciones de bits en $O(1)$ y la instrucción POPCNT, el tiempo se desplomó a solo **147.44 milisegundos**.  
> 
> Las métricas inferiores resumen la contundencia de los hallazgos:  
> - **-99.23%** de poda combinatoria gracias a MRV.  
> - **Identidad exacta** de decisiones (14,672 backtracks).  
> - Y una **aceleración global de 258.2 veces** entre el Nivel 1 y el Nivel 3. Nuestro sistema resuelve en una fracción de segundo lo que al método secuencial le toma cerca de 40 segundos."

---

### [DIAPOSITIVA 12: CONCLUSIONES Y TRABAJO FUTURO]
*(Tiempo: 09:45 - 10:30)*  
*(Indicación: Cambiar a Diapositiva 12. Tono firme y concluyente).*

**Riveros:**  
> "Para sintetizar nuestro trabajo del Segundo Hito, arribamos a tres conclusiones fundamentales:  
> 
> 1. **Eficacia y Escalabilidad del Modelado en Grafos:** Abstraer las restricciones del Sudoku a un grafo regular simple ($|V| = 2,401$ y $|E| = 158,466$ para $k=7$) mediante Listas de Adyacencia en conjuntos hash (`set`) permite verificar colisiones en tiempo $O(1)$ promedio consumiendo solo 1.25 MB de memoria RAM. Esto superó la ineficiencia de matrices densas y cumplió con creces las cuotas exigidas de más de 800 nodos por integrante.  
> 
> 2. **Impacto Algorítmico y Sinergia de Hardware:** Se demostró cuantitativamente que la heurística informada MRV poda el 99.23% del árbol combinatorio al fallar primero, y que la integración de vectores de bits y la instrucción POPCNT de la CPU provee una aceleración de 258×, logrando respuestas en tiempo real imperceptibles para el ojo humano.  
> 
> 3. **Ingeniería de Software y Proyección al Hito 3:** La arquitectura MVC desacoplada integró exitosamente la GUI interactiva, la telemetría en vivo y el soporte multi-escala dinámico de 4×4 a 16×16.  
> Como trabajo futuro proyectado para el Hito 3, nos proponemos implementar el algoritmo de **Consistencia de Arcos (AC-3)** para pre-podar dominios antes de la búsqueda, así como la heurística **LCV (Least Constraining Value)** para optimizar el ordenamiento de valores en tableros de escala superior como $25 \times 25$ y $49 \times 49$."

---

### [DIAPOSITIVA 13: CIERRE, REPOSITORIO Y PREGUNTAS]
*(Tiempo: 10:30 - 11:00)*  
*(Indicación: Cambiar a Diapositiva 13. Invitar al equipo a encender micrófonos/cámaras y abrir la ronda de preguntas).*

**Riveros:**  
> "Ponemos a disposición de la cátedra el repositorio oficial en GitHub con todo el código fuente modular, los datasets generados, la suite de pruebas unitarias automatizadas con 100% de cobertura y la documentación técnica completa.  
> 
> Agradecemos sinceramente la atención del profesor José Luis Soncco Alvarez y de los presentes. Quedamos a su entera disposición para responder a las preguntas que estime pertinentes.  
> 
> Muchas gracias."

---

## BANCO DE PREGUNTAS ANTICIPADAS PARA LA DEFENSA ORAL (Q&A)

A continuación se detallan las respuestas modelo ante las preguntas técnicas más probables formuladas por el docente en la sustentación individual:

---

### PREGUNTA 1 (Dirigida a Kobashigawa):
**Docente:** *"En la Diapositiva 4 ustedes afirman que el grafo tiene 158,466 aristas. ¿Cómo demuestran matemáticamente que ese número es exacto y no contiene aristas duplicadas ni faltantes?"*

**Respuesta de Kobashigawa:**  
> "Profesor Soncco, la demostración se fundamenta en el **Lema del Apretón de Manos (Handshaking Lemma)** de la teoría de grafos, el cual postula que para todo grafo no dirigido simple, la suma de los grados de todos los vértices es exactamente igual al doble del número de aristas:  
> $\sum_{v \in V} d(v) = 2|E|$  
> 
> Como demostramos formalmente, nuestro grafo para $k=7$ ($N=49$) es un grafo **132-regular**. Cada celda comparte fila con 48 celdas, columna con otras 48, y su subcuadrícula de $7 \times 7$ añade $(7-1)^2 = 36$ celdas no colineales. Al sumar $48 + 48 + 36$, obtenemos un grado idéntico de $d(v) = 132$ para cada uno de los 2,401 vértices.  
> 
> Al multiplicar $2,401 \times 132$, la suma total de grados es exactamente **316,932**. Dividiendo entre 2 para descontar la bidireccionalidad de las aristas, obtenemos:  
> $|E| = \frac{316,932}{2} = 158,466$.  
> Además, en nuestro script de generación (`src/model.py`), implementamos la inserción mediante pares ordenados $u < v$ y verificamos con aserciones unitarias en `test_model.py` que la cantidad de aristas en el CSV coincida exactamente con este valor teórico."

---

### PREGUNTA 2 (Dirigida a Pareja):
**Docente:** *"¿Por qué afirman que la heurística MRV reduce la complejidad práctica sin comprometer la completitud del algoritmo? ¿Existe algún caso donde MRV no encuentre solución si esta existe?"*

**Respuesta de Pareja:**  
> "No, profesor Soncco. La heurística MRV pertenece a la familia de algoritmos de **búsqueda sistemática exacta y completa**.  
> 
> MRV modifica exclusivamente el **orden de selección de las variables** (qué celda evaluar primero en el árbol de recursión), pero no poda ninguna rama que contenga una asignación potencialmente válida.  
> 
> La razón por la que acelera el proceso es el principio **'Fail-First'**: al elegir siempre la celda que tiene el menor dominio $|D(v)|$, si dicha celda solo tiene una opción, se reduce de inmediato el factor de ramificación local a 1. Y si en alguna rama una celda se queda sin opciones ($|D(v)| = 0$), se detecta la inconsistencia de inmediato y se retrocede antes de ramificar en celdas irrelevantes.  
> 
> Por tanto, el espacio de búsqueda que MRV elimina corresponde en un 100% a **subárboles inconsistentes y callejones sin salida**, garantizando que si existe una solución válida, MRV la encontrará indefectiblemente."

---

### PREGUNTA 3 (Dirigida a Pareja):
**Docente:** *"Explique con mayor detalle cómo funciona la instrucción POPCNT en el Nivel 3. ¿Cómo una función de Python como `int.bit_count()` logra ejecutarse en $O(1)$ de hardware?"*

**Respuesta de Pareja:**  
> "En Python 3.10 en adelante, la biblioteca estándar introdujo el método `int.bit_count()` implementado en C a bajo nivel en la máquina virtual CPython.  
> 
> Cuando este código es compilado y ejecutado en procesadores modernos que soportan el set de instrucciones **SSE4.2 en arquitectura x86-64** (o la extensión NEON en ARM), CPython utiliza la función intrínseca `__builtin_popcount` del compilador GCC o MSVC. Esto emite directamente el opcode binario de la instrucción de hardware **`POPCNT`**.  
> 
> En lugar de requerir un bucle de software que desplace bits iterativamente en tiempo $O(N)$ o consulte una tabla en memoria, la circuitería aritmética de la ALU del procesador calcula la cantidad de bits en estado alto en **un solo ciclo de reloj**.  
> 
> En nuestro algoritmo, para saber cuántos candidatos le quedan a una celda, hacemos `disponibles.bit_count()`, obteniendo la cantidad exacta de opciones en tiempo estrictamente constante $O(1)$."

---

### PREGUNTA 4 (Dirigida a Riveros):
**Docente:** *"En la Tabla 1 de resultados, ¿por qué los retrocesos del Nivel 2 y del Nivel 3 son exactamente idénticos (14,672 backtracks), pero el tiempo baja de 3,571 ms a 147 ms?"*

**Respuesta de Riveros:**  
> "Ese resultado es precisamente la mayor prueba de rigor científico de nuestra investigación, profesor Soncco.  
> 
> Demuestra que el **Nivel 2 y el Nivel 3 recorren exactamente el mismo árbol de búsqueda**. Ambos algoritmos toman idénticas decisiones heurísticas y evalúan las celdas en el mismo orden lógico porque ambos implementan la heurística MRV. Por ello, la cantidad de decisiones y retrocesos es idéntica: exactamente 14,672.  
> 
> La diferencia radical en el tiempo —que baja de 3.5 segundos a solo 147 milisegundos, una aceleración de 24 veces— se debe exclusivamente a la **complejidad temporal de cada paso individual**:
> - En el Nivel 2, en cada nodo se realizaban operaciones de conjuntos (`set.intersection` y `len()`), lo que involucra asignaciones dinámicas de memoria y búsqueda hash.
> - En el Nivel 3, esas operaciones fueron sustituidas por álgebra booleana sobre enteros (`&`, `|`, `~`) y la instrucción de hardware POPCNT.  
> Al reducir el costo de cada visita de microsegundos a nanosegundos en hardware, la acumulación a lo largo de 14,672 pasos produce la reducción del tiempo a solo 147 ms."

---

### PREGUNTA 5 (Dirigida a todo el equipo o individual):
**Docente:** *"¿Cómo garantizaron que el trabajo fuera distribuido equitativamente entre los tres miembros del equipo y cómo se evidencia esto en el código?"*

**Respuesta conjunta:**  
> "Profesor, el trabajo se planificó y ejecutó de manera estrictamente modular y colaborativa a través de GitHub:  
> - **Kobashigawa** lideró la fundamentación teórica, la revisión de literatura sobre NP-completitud, la formulación matemática del grafo y la partición individual del dataset, responsabilizándose de los primeros 800 nodos en `sudoku_nodes.csv` y la generación de la Figura 1.  
> - **Pareja** se encargó del diseño y optimización del motor algorítmico en `src/solver.py`, desarrollando los tres niveles (DFS, MRV y Bitmasks O(1)) y realizando las demostraciones asintóticas Big-O temporales y espaciales.  
> - **Riveros** lideró el diseño de la arquitectura de software MVC, el modelado del diagrama de clases UML, el desarrollo integral de la interfaz gráfica interactiva en `src/main.py`, la suite de pruebas unitarias automatizadas (`tests/test_model.py`) y el protocolo de benchmarking experimental.  
> 
> Esta distribución se encuentra reflejada con total transparencia en el historial de commits y branches de nuestro repositorio oficial de GitHub."

---
*Fin del Guión Oficial de Exposición TB2 — Grupo 5 (UPC 2026-20)*
