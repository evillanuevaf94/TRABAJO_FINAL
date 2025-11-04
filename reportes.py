import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Rutas de archivos
dataset = pd.read_excel('clientes_lineas.xlsx')
dataset.to_csv('clientes_lineas.csv', index=False)
dataset = pd.read_csv('clientes_lineas.csv')

# Estadísticas descriptivas
resumen = dataset[["MontoLinCre ($)", "MontoLinCre (S/)"]].describe()
resumen.to_excel("estadisticas.xlsx")
# Cantidad de clientes por funcionario
clientes_oficina = (
        dataset.groupby("Oficina")["RazonSocial"]
        .nunique()  # cuenta clientes únicos por oficina
        .sort_values(ascending=False)
    )
# Crear gráfico de barras
plt.figure(figsize=(8, 5))
sns.barplot(x=clientes_oficina.index, y=clientes_oficina.values, palette="Blues_r")
plt.title("Cantidad de clientes por oficina")
plt.xlabel("Oficina")
plt.ylabel("Total de clientes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Guardar imagen en la carpeta OUTPUT_PATH
plt.savefig("clientes_por_oficina.png", bbox_inches="tight")
plt.close()
  

#Montos total para estado activo y vencido
montos = dataset.groupby("EstadoLinCre")["MontoLinCre ($)"].sum()
plt.pie(
        montos,
        labels=[f"{estado}\n${valor:,.0f}" for estado, valor in zip(montos.index, montos.values)],  # etiquetas con monto
        autopct="%1.1f%%",          # porcentaje con 1 decimal
    )
plt.title("Distribución del Monto de Líneas de Crédito por Estado")
plt.savefig("montos_por_estado_pie.png", bbox_inches="tight")
plt.close()
print("Reportes generados")