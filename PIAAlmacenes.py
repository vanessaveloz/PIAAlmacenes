import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url_concierto="https://raw.githubusercontent.com/myAle27admin/PIA_AlmacenesDatos/refs/heads/main/concierto_asistentes.csv"
asistentes=pd.read_csv(url_concierto)

def información_general():
    print("=" * 55)
    print("--- Información general del conjunto de datos ---")
    print("-" * 50)
    asistentes.info()
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")

def primeras_ultimas_filas():
    print("=" * 55)
    print("\t\t\t\t\t--- Primeras 5 filas de registros ---")
    print("-" * 108)
    print(asistentes.head())
    print("\n")
    print("\t\t\t\t\t--- Ultimas 5 filas de registros ---")
    print("-" * 115)
    print(asistentes.tail())
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")
            
def estadisticos():
    print("=" * 55)
    print("\t--- Resumen estadístico de las columnas numéricas ---")
    print("-" * 70)
    print(asistentes.describe())
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")

def valores_nulos():
    print("=" * 55)
    print("--- Existencia de valores nulos ---")
    print("-" * 35)
    print(asistentes.isnull().sum())
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")
            
def variables_categoricas():
    print("=" * 55)
    print("--- Conteo de valores por categoría ---")
    print("-" * 40)
    print(asistentes['género'].value_counts())
    print()
    print(asistentes['tipo_boleto'].value_counts())
    print()
    print(asistentes['sección'].value_counts())
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")
            
def distribución_edades():
    print("Mostrando gráfica...")
    plt.figure(figsize=(8, 5))
    sns.histplot(asistentes['edad'], kde=True, bins=20, color='blue')
    plt.title('Distribución de edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
def distribución_genero():
    print("Mostrando gráfica...")
    plt.figure(figsize=(6, 4))
    asistentes['género'].value_counts().plot(kind='bar', color='orange')
    plt.title('Distribución por género')
    plt.xlabel('Género')
    plt.ylabel('Frecuencia')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
def precio_tipo_boleto():
    print("Mostrando gráfica...")
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='tipo_boleto', y='precio_boleto', data=asistentes)
    plt.title('Precio del boleto por tipo')
    plt.xlabel('Tipo de boleto')
    plt.ylabel('Precio del boleto')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
def relacion_edad_precio_boleto():
    print("Mostrando gráfica...")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='edad', y='precio_boleto', hue='tipo_boleto', data=asistentes)
    plt.title('Relación entre edad y precio del boleto')
    plt.xlabel('Edad')
    plt.ylabel('Precio del boleto')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
def asistencia_tipo_boleto():
    print("=" * 55)
    print("--- Media de asistencia por tipo de boleto ---")
    print("-" * 40)
    asistencia_por_boleto = asistentes.groupby('tipo_boleto')['asistió'].mean()
    print(asistencia_por_boleto)
    print()
    print("Mostrando gráfica...")
    asistencia_por_boleto.plot(kind='bar', color='green')
    plt.title('Tasa de asistencia por tipo de boleto')
    plt.xlabel('Tipo de boleto')
    plt.ylabel('Proporción de asistencia')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")
            
def correlacion_numerica():
    print("=" * 55)
    print("--- Media de asistencia por tipo de boleto ---")
    print("-" * 40)
    correlation_matriz = asistentes[['edad', 'precio_boleto', 'fila_asiento', 'asistió']].corr()
    print(correlation_matriz)
    print()
    print("Mostrando gráfica...")
    plt.figure(figsize=(8, 5))
    sns.heatmap(correlation_matriz, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de correlación')
    plt.show()
    print()
    print("Cerrando gráfica...")
    
    while True:
        print()
        opcion = input("¿Deseas volver? (1 para volver): ")

        if opcion == "1":
            print("Regresando...")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")

def menu_principal():
    while True:
        print("=" * 55)
        print("\t--- Análisis Exploratorio de Datos ---")
        print("-" * 55)
        print("1. Información general")
        print("2. Primeras y últimas filas de registros")
        print("3. Resumen estadístico")
        print("4. Conteo de valores nulos")
        print("5. Conteo de variables categóricas")
        print("6. Grafica de Distribución de edades")
        print("7. Grafica de Distribución por género")
        print("8. Grafica de Precio del boleto por tipo")
        print("9. Grafica de Relación entre edad y precio del boleto")
        print("10. Asistencia por tipo de boleto")
        print("11. Correlación de variables numericas")
        print("12. Salir")
        print("=" * 55)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            información_general()
        elif opcion == '2':
            primeras_ultimas_filas()
        elif opcion == '3':
            estadisticos()
        elif opcion == '4':
            valores_nulos()
        elif opcion == '5':
            variables_categoricas()
        elif opcion == '6':
            distribución_edades()
        elif opcion == '7':
            distribución_genero()
        elif opcion == '8':
            precio_tipo_boleto()
        elif opcion == '9':
            relacion_edad_precio_boleto()
        elif opcion == '10':
            asistencia_tipo_boleto()
        elif opcion == '11':
            correlacion_numerica()
        elif opcion == '12':
            print("Saliendo...")
            break
        else:
            print("Opción no valida. Intente nuevamente.")

menu_principal()