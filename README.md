# Prueba Técnica
Prueba técnica para el puesto de desarrollador en la sección de Evolución Financiación en Bancolombia, consiste en un programa para extraer datos de una base en excel, realizar un procesamiento y crear tablas calculadas para obtener estadísticas sobre las ventas de una empresa.

# 📊 Procesador y Generador de Reportes de Ventas

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-brightgreen.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-yellow.svg)](https://matplotlib.org/)
[![Openpyxl](https://img.shields.io/badge/Openpyxl-3.1+-orange.svg)](https://openpyxl.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Descripción 📄

**Procesador y Generador de Reportes de Ventas** es un script en Python que permite automatizar la carga, limpieza, análisis y generación de reportes de datos de ventas en archivos Excel.

Este programa realiza un procesamiento de datos que incluye:
- Limpieza y validación de los datos de ventas.
- Conversión de fechas y agregación por mes y vendedor.
- Cálculo de estadísticas de ventas por vendedor y por mes.
- Generación de gráficos de ventas y exportación a imágenes.
- Creación de un reporte Excel con los resúmenes y gráficos embebidos.

El objetivo es facilitar el análisis y la presentación de los resultados comerciales de manera clara y visual.

---

## Características 🚀

- ✅ Procesamiento automático de datos de ventas.
- ✅ Generación de gráficos de ventas por vendedor y por mes.
- ✅ Exportación a archivos Excel con gráficos integrados.
- ✅ Manejo de errores en la carga y el procesamiento de datos.
- ✅ Modular y extensible para otros tipos de reportes.

---

## Requisitos ✅

| Paquete     | Versión recomendada |
|-------------|---------------------|
| Python      | 3.10 o superior     |
| pandas      | 2.0.0 o superior    |
| matplotlib  | 3.7.0 o superior    |
| openpyxl    | 3.1.0 o superior    |

---
# Estructura del Código

A continuación se muestra la estructura del código y las principales clases y métodos implementados:

## Clases

### `procesador_de_ventas`
Esta clase se encarga de:
- Cargar y preprocesar el DataFrame de ventas.
- Validar y limpiar los datos.
- Convertir datos de fecha y agregar campos adicionales.
- Calcular estadísticas de ventas por vendedor y por mes.
- Generar gráficos correspondientes.

#### Métodos:
- **`__init__(self, ruta_archivo_ventas)`**  
  Inicializa la clase, carga los datos y ejecuta el procesamiento completo.

- **`cargar_dataframe(self, ruta_archivo_ventas)`**  
  Carga el archivo Excel en un DataFrame.

- **`obtener_campos_requeridos(self)`**  
  Extrae las columnas requeridas del DataFrame.

- **`preprocesar_datos(self)`**  
  Limpia y valida los datos; calcula el total de ventas donde falte información.

- **`convertir_fecha_datetime(self)`**  
  Convierte la columna de fecha a formato datetime.

- **`agregar_campo_mes(self)`**  
  Agrega una columna para el mes derivado de la fecha.

- **`filtrar_ventas_por_annio(self, annio)`**  
  Filtra las ventas correspondientes al año especificado.

- **`calculo_estadistico_ventas_vendedor(self)`**  
  Calcula el total de ventas agrupado por vendedor.

- **`calculo_estadistico_ventas_mes(self)`**  
  Calcula el total de ventas agrupado por mes.

- **`graficar_ventas_vendedores(self)`**  
  Genera y guarda un gráfico de barras para las ventas por vendedor.

- **`graficar_ventas_mes(self)`**  
  Genera y guarda un gráfico de líneas para las ventas por mes.

---

### `generador_reporte`
Esta clase se encarga de:
- Generar reportes en Excel a partir de los datos procesados.
- Incluir gráficos en el reporte Excel.

#### Métodos:
- **`__init__(self, procesados, ruta_archivo_reporte)`**  
  Inicializa la clase, genera los reportes y exporta el archivo Excel.

- **`generar_reporte_ventas_vendedores(self)`**  
  Genera un reporte con el total de ventas por vendedor.

- **`generar_reporte_ventas_mes(self)`**  
  Genera un reporte con el total de ventas por mes.

- **`exportar_archivo_resumen(self, ruta_archivo_reporte)`**  
  Exporta los datos a un archivo Excel con hojas separadas para cada reporte.

- **`insertar_graficos_en_archivo_resumen(self, ruta_archivo_reporte)`**  
  Inserta los gráficos generados en las hojas correspondientes del Excel.
