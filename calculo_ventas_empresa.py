import pandas as pd
import datetime

class procesador_de_ventas:

    def __init__(self, ruta_archivo_ventas):
        self.df_ventas = self.cargar_dataframe(ruta_archivo_ventas)
        self.obtener_campos_requeridos()
        self.preprocesar_datos()
        self.convertir_fecha_datetime()
        self.agregar_campo_mes()
        self.filtrar_ventas_por_annio(2023)
        self.calculo_estadistico_ventas_vendedor()

    def cargar_dataframe(self,ruta_archivo_ventas):
        try:
            return pd.read_excel(ruta_archivo_ventas)
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de ventas no fue encontrado en la dirección ingresada.")

    def obtener_campos_requeridos(self):
        campos_requeridos = ['ID_Venta','Fecha','Producto','Cantidad','Precio_Unitario','Total_Venta','Vendedor'] # Lista para ingresar los campos que quiero en el dataframe, permite agregar y campos en caso de que el archivo excel de ventas traiga nuevso campos en el futuro.
        try:
            self.df_ventas = self.df_ventas.loc[:,campos_requeridos]
        except KeyError as e:
            print("Error: No se a encontrado una o más columnas en el Dataframe.")
            print(f"Detalles del error: {e}")


    def preprocesar_datos(self):

        try:
            total_venta_vacios = self.df_ventas['Total_Venta'].isna() #obtengo los registros de Total_Venta que están vacíos para usarlos como filtro
            self.df_ventas.loc[total_venta_vacios,'Total_Venta'] = ( self.df_ventas[total_venta_vacios]['Cantidad'] * self.df_ventas.loc[total_venta_vacios]['Precio_Unitario'] ) #Con el filtro de registros vacíos tomo cada campo Total_Venta y lo calculo usando su respectivo registro de Cantidad y Precio Unitario con una multiplicación.

            self.df_ventas['Producto'] = self.df_ventas['Producto'].astype('category') #Convertimos el campo Producto a categoría debido a que es más conveniente en campos de variables limitadas como este.
        except KeyError as ke:
            print(f"Error no se encuentra el campo en el dataframe: {ke}")

        except TypeError as te:
            print(f"Error de incompatibilidad en el tipo de dato: {te}")
        except Exception as e:
            print(f"Ocurrio un Error no esperado: {e}")


    def convertir_fecha_datetime(self):
        try:
            self.df_ventas['Fecha'] = pd.to_datetime(self.df_ventas['Fecha'],errors='coerce') #Convierte a datetime las fechas de la columna Fecha y en caso de no poder convertir algún valor lo deja como NaT que equivale a un NaN en fechas.
        except KeyError:
            print("Error, la columna 'Fecha' no se encontró en el dataframe.")
        except Exception as e:
            print(f"Ocurrió un error no esperado: {e}")

    def agregar_campo_mes(self):
        try:
            self.df_ventas['Mes'] = self.df_ventas['Fecha'].dt.month
        except KeyError:
            print("Error, no se pudo encontrar el campo 'Mes' en el dataframe.")
        except Exception as e:
            print(f"Ocurrió un error no esperado: {e}")
    
    def filtrar_ventas_por_annio(self, annio):
        try:
            self.df_ventas = self.df_ventas[self.df_ventas['Fecha'].dt.year == annio]

        except KeyError as ke:
            print(f"Error al encontrar el campo: {ke}") #Capturo error en caso de no encontrar el campo

        except AttributeError as te:
            print(f"Campo Fecha no esta en el formato indicado de fecha {te}")#Capturo el error en caso de que pandas no pueda acceder al atributo dt de datetime

        except Exception as e:
            print(f"[Error inesperado] {e}")

    def calculo_estadistico_ventas_vendedor(self):
        try:
            self.df_ventas_por_vendedor = self.df_ventas.groupby('Vendedor')['Total_Venta'].sum().reset_index()
        except Exception as e:
            print(f"Ocurrió un error no esperado: {e}")

    def calculo_estadistico_ventas_mes(self):
        pass


if __name__ == "__main__":
    procesador_ventas = procesador_de_ventas('datos_ventas.xlsx')