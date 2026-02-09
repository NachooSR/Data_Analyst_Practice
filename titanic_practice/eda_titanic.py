import pandas as pd

data_frame= pd.read_csv("titanic_filtered.csv")


def count_survivers(data: pd.DataFrame)-> float :
    supervivientes= data_frame["Survived"].sum()
    porcentaje= float((supervivientes * 100)/ len(data_frame) ).__round__()
    return porcentaje


def age_mean_survivers(data: pd.DataFrame)-> tuple[float,float]:
    
    age_mean= data["Age"].mean().__round__()
    age_mean_survivers= data[data["Survived"]==True]["Age"].mean().__round__()
    return age_mean,age_mean_survivers


def label_age(age: float):
    if age < 15:
        return "Child"
    elif age < 25:
        return "Teen"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

def categorize_age(data: pd.DataFrame) -> pd.DataFrame :
    data["Group_age"]= data["Age"].apply(label_age)
    return data

def group_surviver(data: pd.DataFrame):
    data= data.groupby("Group_age")["Survived"].sum()
    return data


def tasa_supervivencia(data_group: pd.DataFrame, group_trip: pd.DataFrame)-> pd.Series:
    percent_survivers= (group_survivers / group_trip) *100
    percent_survivers= percent_survivers.round(2).sort_values(ascending=False)
    return percent_survivers

# 1- Conclusion -> Porcentaje de supervivientes
print(f"\nSupervivientes: {count_survivers(data_frame):.2f}%\n")

# 2- Conclusion -> Edad tripulantes/ Edad supervivientes
edad_promedio,promedio_supervivientes= age_mean_survivers(data_frame)
print(f"\nLa edad promedio de la tripulacion es: {edad_promedio}")
print(f"Edad promedio supervivientes: {promedio_supervivientes}\n")


# 3- Grupos etarios
data_frame= categorize_age(data_frame) # Les ponemos etiquetas segun su grupo
print("Cuantos tripulantes hay de cada grupo:\n")
tripulantes_group_age=data_frame["Group_age"].value_counts() # Cantidad de tripulantes por grupo
print(tripulantes_group_age)

# 3a- Grupos etarios -> SUPERVIVIENTES
group_survivers= group_surviver(data_frame)
print(f"\nSobrevivieron: {data_frame["Survived"].sum()} personas, repartidas de la siguiente manera")
print("\n",group_survivers)

# 4- Tasa de supervivencia segun grupo
percent_survivers = tasa_supervivencia(group_survivers,tripulantes_group_age)

print("\nTasa de supervivencia por grupo etario: ")
print(percent_survivers)

