# Extracción de Productos desde un Archivo HTML

## Descripción
Este script está diseñado para extraer nombres de productos y URLs de imágenes desde un archivo HTML (`kemik.html`). Los datos procesados se exportan a un archivo CSV estructurado (`productos_limpios.csv`), facilitando su uso posterior en análisis o integraciones.

## Funcionamiento
1. **Lectura del archivo HTML**: Se abre y se lee el contenido de `kemik.html`.
2. **Extracción de datos**: Se utilizan expresiones regulares para obtener:
   - Nombres de productos a partir del atributo `alt` en las etiquetas `<img>`.
   - URLs de imágenes desde el atributo `src`.
3. **Procesamiento de URLs**: Las URLs de las imágenes son limpiadas para eliminar información innecesaria.
4. **Validación**: El script verifica que el número de nombres de productos coincida con el número de URLs procesadas.
5. **Exportación a CSV**: Los datos se guardan en un archivo llamado `productos_limpios.csv`.

## Parámetros
- **Archivo de entrada**:
  - `kemik.html`: Archivo HTML que contiene los datos de productos.
- **Archivo de salida**:
  - `productos_limpios.csv`: Archivo CSV que contendrá las URLs de las imágenes y los nombres de los productos.

## Uso
1. Coloca el archivo `kemik.html` en el mismo directorio que el script.
2. Ejecuta el script con el siguiente comando:
   ```bash
   python web.py
