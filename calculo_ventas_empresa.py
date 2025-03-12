import pandas as pd
import datetime

class procesador_de_ventas:

    def __init__(self, ruta_archivo_ventas):
        self.df_ventas = self.cargar_dataframe(ruta_archivo_ventas)
        self.obtener_campos_requeridos()


    def cargar_dataframe(self,ruta_archivo_ventas):
        try:
            return pd.read_excel(ruta_archivo_ventas)
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de ventas no fue encontrado en la dirección ingresada.")

    def obtener_campos_requeridos(self):
        campos_requeridos = ['ID_Venta','Fecha','Producto','Cantidad','Precio_Unitario','Total_Venta','Vendedor'] # Lista para ingresar los campos que quiero en el dataframe, permite agregar y campos en caso de que el archivo excel de ventas traiga nuevso campos en el futuro.
        self.df_ventas = self.df_ventas.loc[:,campos_requeridos]

    def preprocesar_datos(self):
        pass

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