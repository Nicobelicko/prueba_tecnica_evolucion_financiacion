import pandas as pd
import datetime

class procesador_de_ventas:

    def __init__(self, ruta_archivo_ventas):
        self.df_ventas = self.cargar_dataframe(ruta_archivo_ventas)
        self.obtener_campos_requeridos()
        self.preprocesar_datos()

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

        total_venta_vacios = self.df_ventas['Total_Venta'].isna() #obtengo los registros de Total_Venta que están vacíos para usarlos como filtro
        self.df_ventas.loc[total_venta_vacios,'Total_Venta'] = ( self.df_ventas[total_venta_vacios]['Cantidad'] * self.df_ventas.loc[total_venta_vacios]['Precio_Unitario'] ) #Con el filtro de registros vacíos tomo cada campo Total_Venta y lo calculo usando su respectivo registro de Cantidad y Precio Unitario con una multiplicación.

        self.df_ventas['Producto'] = self.df_ventas['Producto'].astype('category') #Convertimos el campo Producto a categoría debido a que es más conveniente en campos de variables limitadas como este.

    def convertir_fecha_datetime(self):
        pass
    
    def filtrar_ventas_por_annio(self):
        pass

    def calculo_estadistico_ventas_vendedor(self):
        pass

    def calculo_estadistico_ventas_mes(self):
        pass


if __name__ == "__main__":
    procesador_ventas = procesador_de_ventas('datos_ventas.xlsx')