import pandas as pd

'''
Luego de concluir que cuenta el csv y pensar que quiero comparar:
Limpiar el csv:
1- Que cuenta cada columna, se entiende?
2- Valores entendibles?
'''
    

data= pd.read_csv("titanic.csv")
    

# Column Id -> por ahora la dejo como si fuera una db
# Survived -> Seria conveniente en vez de 1 o 0 -> True o False
# Pclass -> renombrar y valores pasar de numerico a texto (primera,segunda y tercera)
# Name -> Limpiar los nombres first + last
# Sex -> bien
# Age -> bien, completar nulos con el promedio de las edades
# SibSp + Parch -> Family members (sum)
# NewColum = Family -> Alone/Family
# Ticket -> Borrar columna (datos distintos)
# Fare -> Cuanto pago. Sirve? -> Borrar
# Cabin -> Muchos datos nulos, dropear
# Embarked -> Desde donde partio reemplazar nombre inicial x nombre ciudad y sino borrar


# Limpieza de columnas
data["Survived"] = data["Survived"].astype(bool)

data.rename(columns={"Pclass":"Person_class"},inplace=True)

# El nombre no nos sirve para las conclusiones que vamos a hacer
data.drop("Name",axis=1,inplace=True)



data["Family_members"]= data["SibSp"] + data["Parch"]

data["Fare"]= data["Fare"].round(2)

# Ya utilizamos las columnas y las borramos
data.drop(["SibSp","Parch","Ticket"],axis=1,inplace=True)



# print(data.isnull().sum()) --> Saber cual es la columna que esta mas vacia
# Eliminamos la columna cabina
data.drop("Cabin",axis=1,inplace=True)

data["Embarked"]= data["Embarked"].replace({"C":"Cherbourg","S":"Southampton","Q":"Queenstown"})

data["Alone"] = data["Family_members"] == 0
data.to_csv("titanic_filtered.csv",index=False)

# Las edades faltantes las vamos a llenar con medianas por grupo

# median_age= (
#     data.groupby(["Sex","Person_class"])["Age"].
#     median()
# )


# Las edades faltantes las vamos a llenar con medianas por grupo
data["Age"]= data["Age"].fillna(
    data.groupby(["Sex","Person_class"])["Age"].transform("median").round()
)

data.to_csv("titanic_filtered.csv",index=False)