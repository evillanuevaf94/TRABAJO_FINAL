import pandas as pd

try:
    # Leer el archivo TXT
    clientes = pd.read_excel('Clientes.xlsx')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv = 'Clientes.csv'
    clientes.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")