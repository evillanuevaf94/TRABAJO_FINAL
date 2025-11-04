import pandas as pd

try:
    # Leer el archivo CSV
    clientes = pd.read_csv('Clientes.csv')
    lineas = pd.read_csv('LineasCredito.csv')

    #Normalizacion
    clientes["RucCliente"] = clientes["RucCliente"].astype(str).str.strip()
    lineas["RucCliente"] = lineas["RucCliente"].astype(str).str.strip()
    # Rellenar valores nulos
    clientes["Funcionario Comercial"] = clientes["Funcionario Comercial"].fillna("Funcionario no registrado")
    lineas["EstadoLinCre"] = lineas["EstadoLinCre"].fillna("Estado no actualizado")
    # Crear columna monto en dolares
    lineas["MontoLinCre ($)"] = lineas["MontoLinCre (S/)"] * 3.39
    # Unir datos de clientes con ventas
    dataset = pd.merge(lineas, clientes, on="RucCliente")
    
    # Exportar a Excel
    archivo_excel = 'clientes_lineas.xlsx'
    dataset.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")