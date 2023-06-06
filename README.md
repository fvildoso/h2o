# H2O - SQL

<br>
Este repositorio contiene un ejemplo de como usar <a href="https://h2o.ai/platform/ai-cloud/make/h2o/">H2O</a> con <a href="https://mariadb.org/">MariaDB</a>. 

## Instrucciones

1. Clonar repositorio con `git clone git@github.com:fvildoso/h2o.git`.

2. Bajar e instalar Java11. Se sugiere usar la distribución de Amazon Corretto:
    - Windows: https://corretto.aws/downloads/latest/amazon-corretto-11-x64-windows-jdk.msi
    - Otros sistemas: https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html
3. Bajar H2O https://h2o-release.s3.amazonaws.com/h2o/rel-zumbo/2/index.html y descomprimir.
4. Bajar driver de MariaDB para Java (versión 3.0.5) desde
   maven: https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.0.5/mariadb-java-client-3.0.5.jar.
   También disponible en carpeta `drivers` de este repositorio.
5. Carga de datos:
    1. Crear esquema de base de datos MariaDB (nombre sugerido de esquema `h2o`).
    2. Cargar CSV `cars_20mpg.csv` (ubicado dentro de la carpeta `data` del repositorio) con opción disponible desde
       PyCharm o DataGrip (se debe crear la conexión al esquema en el panel derecho, puede pedir bajar un driver).
       Debería crear la tabla `cars_20mpg`.
6. Duplicar archivo `.env.example` y renombrar como `.env`. Llenar los valores correspondientes en los datos solicitados
   en el archivo `.env` creado.
7. Crear ambiente virtual (en caso de que PyCharm no lo hubiese creado), e instalar dependencias
   con `pip install -r requirements.txt`.
8. De ser necesario, cambiar los valores de las variables `schema` y `table` en archivo `main_sql.py`
9. Copiar driver descargado en paso 4 en la carpeta donde quedó descomprimido H2O en el paso 3.

   <u>Imagen de referencia 1</u> <img src="media/img.png" alt="example 1">
10. Ejecutar comando en una consola CMD/PowerShell (Windows) o terminal (Max/Linux) en la carpeta donde está
    descomprimido H2O:
    - Windows:
        - CMD: `java -cp h2o.jar;mariadb-java-client-3.0.5.jar water.H2OApp`
        - Powershell: `java -cp "h2o.jar;mariadb-java-client-3.0.5.jar" water.H2OApp`
    - Linux/Mac: `java -cp h2o.jar:mariadb-java-client-3.0.5.jar water.H2OApp`

    Si se quiere ejecutar una segunda vez, el siguiente comando es suficiente `java -jar h2o.jar`

<u>Imagen de referencia 2</u> <img src="media/img_1.png" alt="example 2">

11. No cerrar la terminal ni cancelar la ejecución de H2O. En otra línea de comandos, ejecutar el script
    con `python main_sql.py`; o ejectuar desde PyCharm. En ambos casos, debería mostrar al final en pantalla el AUC.

<img src="media/elmo.jpg" alt="nice">

## Jupyter Playground (opcional)

Una vez completados todos los pasos anteriores (el 11 no es necesario) se puede experimentar con H2O en el
notebook `playground.ipynb`. Si se abre el _notebook_desde PyCharm, automáticamente se ejecuta el servidor local para
usar el _notebook_.

