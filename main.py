import pandas as pd
import numpy as np

def main():
    
    # Carga del data frame
    data_frame= pd.read_csv("data/datos.csv")
    

    #1 - Mostrar las 5 primeras filas
    print(data_frame.head())

    #2- Mostrar empleados mayores a 30
    print(data_frame.loc[data_frame["edad"] > 30, ["nombre","edad"]])

    #3- Salario promedio de todos los empleados
    print(data_frame["salario"].mean())

    #4- Salario promedio por departamento
    print(data_frame.groupby("departamento")["salario"].mean())

    #5- Salario minimo y maximo por departamento
    print(data_frame.groupby("departamento")["salario"].min())

    print(data_frame.groupby("departamento")["salario"].max())

    #6- Edad promedio por departamento
    print(data_frame.groupby("departamento")["edad"].mean())

    #7- Empleados por departamento
    print(data_frame.groupby("departamento")["departamento"].count())

    #8- Empleados salario mayor a 4500
    print(data_frame[data_frame["salario"] >4500])

    #9- Total de salarios por departamento
    print(data_frame.groupby("departamento")["salario"].sum())

    #10- Empleado que mas cobra
    id_max_salary = data_frame["salario"].idxmax()

    print(data_frame.loc[id_max_salary]) 

    #11 - Departamento con mayor promedio de salario
    promedios= data_frame.groupby("departamento")["salario"].mean()
    print(promedios.idxmax())

    #12 - Empleados con antiguedad mayor a 5
    print(data_frame[data_frame["antiguedad"]>5])

    #13- 
    def categorizar_salario(salario):
        if salario <3500:
            return "Bajo"
        elif salario >3500 and salario <4500:
            return "Medio"
        else:
            return "Alto"
        
    data_frame["categoria_salario"]= data_frame["salario"].apply(categorizar_salario)

    print(data_frame)

    #14- Ordenar empleados por salario 
    print(data_frame.sort_values(by= "salario"))

    #15- Bono por antiguedad
    data_frame["bono"]= (
        data_frame["salario"] *
        data_frame["antiguedad"].apply(
            lambda x: 0.1 if x > 5 else 0.05
        )
    )

    #16
    filtrado= data_frame[
        (data_frame["departamento"]== "IT") | 
        (data_frame["departamento"] == "Ventas")
    ]
    print(filtrado["salario"].mean())

main()