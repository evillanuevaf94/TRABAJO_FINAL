import pandas as pd

try:
    print("Iniciando proceso de transformación...")

    # Lectura de archivos
    clientes = pd.read_csv('Clientes.csv')
    lineas = pd.read_csv('LineasCredito.csv')

    # Normalización
    clientes["RucCliente"] = clientes["RucCliente"].astype(str).str.strip()
    lineas["RucCliente"] = lineas["RucCliente"].astype(str).str.strip()

    # Rellenar valores nulos
    clientes["Funcionario Comercial"] = clientes["Funcionario Comercial"].fillna("Funcionario no registrado")
    lineas["EstadoLinCre"] = lineas["EstadoLinCre"].fillna("Estado no actualizado")

    # Crear columna de monto en dólares
    lineas["MontoLinCre ($)"] = lineas["MontoLinCre (S/)"] * 3.39

    # Unir datos
    dataset = pd.merge(lineas, clientes, on="RucCliente")

    # Validación básica
    total_clientes = dataset["RucCliente"].nunique()
    total_funcionarios = dataset["Funcionario Comercial"].nunique()
    print(f"Total de clientes procesados: {total_clientes}")
    print(f"Total de funcionarios comerciales: {total_funcionarios}")

    # Exportar resultados
    archivo_excel = 'clientes_lineas.xlsx'
    dataset.to_excel(archivo_excel, index=False)
    print(f"Datos transformados exportados a {archivo_excel}")

    # Generar un reporte resumen
    resumen = dataset.groupby("Funcionario Comercial")[["MontoLinCre (S/)", "MontoLinCre ($)"]].sum().reset_index()
    resumen.to_excel("reporte_resumen_funcionarios.xlsx", index=False)
    print("Reporte resumen generado: reporte_resumen_funcionarios.xlsx")

    print("Transformación finalizada correctamente.")

except Exception as e:
    print(f"Error durante la transformación: {e}")



    