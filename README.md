# conflictos


# Pregunta de control 1: ¿Por qué es necesario realizar un "clone" al inicio en lugar de simplemente copiar el archivo manualmente?

Porque git clone no solo descarga los archivos, sino que:

Crea la carpeta .git con todo el historial del proyecto.

Conecta tu proyecto con el repositorio remoto.

Permite usar comandos como pull, push, fetch, merge, etc.

Si solo copias el archivo, no existe ningún vínculo con GitHub y no puedes colaborar ni sincronizar cambios.

# Pregunta de control 2: En PyCharm, ¿qué indicador visual te confirma que tu proyecto está vinculado correctamente a un repositorio Git?
En la esquina inferior derecha aparece el texto:
Git: master o Git: main.

Además, los archivos cambian de color:

Azul: archivo modificado

Verde: archivo nuevo

Rojo: archivo eliminado

# Pregunta de control 1: ¿Qué ocurre exactamente al hacer un push si alguien ya realizó y subió un cambio en la misma zona del código? 
Git rechaza el push mostrando un error tipo:

rejected – non-fast-forward

Esto ocurre porque tu repositorio local está desactualizado y no contiene los cambios que ya están en el remoto.
# Pregunta de control 2: ¿Por qué Git no decide automáticamente que el último push es el válido? 

Porque Git no entiende la lógica del código.

No puede saber si:

resultado = a + b


es mejor que:

resultado = a * b


Ambas versiones son válidas técnicamente, pero solo un humano puede decidir cuál tiene sentido funcional.
# Pregunta de control 1: ¿Cómo definirías un "conflicto" en Git basándote en lo que acabas de ver en la herramienta de PyCharm? 
Un conflicto ocurre cuando:

Dos personas modifican la misma parte del mismo archivo, y Git no puede combinarlas automáticamente sin perder información.

Es una situación donde Git se detiene y exige una decisión humana.
# Pregunta de control 2: ¿Qué pasos debes seguir en el IDE tras aceptar los cambios para que la resolución sea definitiva en el repositorio remoto?
Usar la herramienta visual y elegir el contenido final.

Guardar el archivo.

Marcarlo como resuelto:

PyCharm lo hace automáticamente al guardar sin marcas de conflicto.

Hacer:

Commit con un mensaje tipo:
Resolución de conflicto en calculadora.py

Hacer Push al repositorio remoto.

# Pregunta de control 1: ¿Qué estrategia o flujo de trabajo (workflow) consideráis más efectivo para evitar conflictos constantes en un equipo grande? 
Workflow recomendado: Ramas por funcionalidad (Feature Branches)

Cada persona trabaja en su propia rama:

feature-suma

feature-multiplicacion

Solo se fusiona con main cuando:

El código está probado.

No hay conflictos graves.

Además:

Hacer pull antes de empezar a programar.

Dividir el trabajo en archivos o funciones distintas.

Comunicación constante:
“Estoy tocando calculadora.py, línea 5”.

Esto reduce drásticamente los conflictos y mejora la calidad del proyecto.