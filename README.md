# Extracción de Datos de Archivos DXF
Este proyecto proporciona un script en Python para extraer datos de archivos DXF y guardarlos en un nuevo archivo DXF con formato específico.

Descripción
El script extrae datos de varios tipos de entidades presentes en archivos DXF, como líneas, círculos, arcos, polilíneas, texto, dimensiones, etc. Luego, utiliza estos datos para crear un nuevo archivo DXF con las mismas entidades, formateadas según un formato específico.

Características
Extracción de datos: El script puede extraer datos de una amplia variedad de entidades presentes en archivos DXF.
Formato personalizado: Permite definir un formato específico para las entidades en el nuevo archivo DXF.
Soporte para múltiples tipos de entidades: El script puede manejar diferentes tipos de entidades presentes en archivos DXF, incluidas las entidades 2D y 3D.
Fácil de usar: Simplemente proporciona la ruta del archivo DXF de entrada y el script generará automáticamente el archivo DXF de salida con los datos extraídos.

Requisitos
Python 3.x
Biblioteca ezdxf

python extract_dxf_data.py ruta/del/archivo.dxf
El script generará un nuevo archivo DXF con los datos extraídos y formateados según el formato especificado.
Tambien genera la salida de los vectores del archivo .dxf
