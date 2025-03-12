import pandas as pd
import datetime

class procesador_de_ventas:

    def __init__(self, ruta_archivo_ventas):
        self.df_ventas = self.cargar_dataframe(ruta_archivo_ventas)



    def cargar_dataframe(self,ruta_archivo_ventas):
        try:
            return pd.read_excel(ruta_archivo_ventas)
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de ventas no fue encontrado en la dirección ingresada.")

    def obtener_campos_requeridos(self):
        pass

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