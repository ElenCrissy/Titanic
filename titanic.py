import pandas

train = pandas.read_csv('train.csv')
nb_survived = train.query(expr="Survived==1")
print("survivants :", len(nb_survived)) 
nb_deceased = train.query(expr="Survived==0")
print("morts :", len(nb_deceased))

#Recherche si la colonne Survived contient des valeurs nulles
survived_null = len(train.isna().query(expr="Survived == False"))
print("nb valeurs nulles pour colonne Survived", survived_null)

#Vérifier qu'il n'ya pas de valeurs nulles pour l'âge
survived_null = len(train.isna().query(expr="Age == True"))
print("nb valeurs nulles spour colonnes Age", survived_null)

#Calcul moyenne d'âge des passagers
mean_age=round (train["Age"].mean())
print("age moyen :", mean_age)

# Pour les valeurs nulles, on remplace par la valeur moyenne pour modifier de façon importante les données 
# inplace permet de modifier de façon permanente la colonne
print(train['Age'].head(10))
train.Age.fillna(mean_age, inplace=True)
print(train['Age'].head(10))

#Afficher le nb personne dans chacune des classes
nb_person_class3 = train.query(expr="Pclass == 3")
print("passagers classe 3", len(nb_person_class3))
nb_person_class3_deceased = train.query(expr="Pclass == 3 and Survived==0")
print("passagers classe 3 décédé", len(nb_person_class3_deceased))

nb_person_class2 = train.query(expr="Pclass == 2")
print("passagers classe 2", len(nb_person_class2))
nb_person_class2_deceased = train.query(expr="Pclass == 2 and Survived==0")
print("passagers classe 2 décédé", len(nb_person_class2_deceased))

nb_person_class1 = train.query(expr="Pclass == 1")
print("passagers classe 1", len(nb_person_class1))
nb_person_class1_deceased = train.query(expr="Pclass == 1 and Survived==0")
print("passagers classe 1 décédé", len(nb_person_class1_deceased))

print("décédés classe 3 :", round(len(nb_person_class3_deceased)/len(nb_person_class3)*100), "%")
print("décédés classe 2 :", round(len(nb_person_class2_deceased)/len(nb_person_class2)*100), "%")
print("décédés classe 1 :", round(len(nb_person_class1_deceased)/len(nb_person_class1)*100), "%")


# Remplacer "Male" et "Female" par 1 pour "male" et 0 pour "female"
# les bibliothèques numpy et pandas ne travaillent que sur des valeurs numériques

# Supprimer les colonnes qui ne seront pas utilisées contenant des valeurs textuelles ou ne semblant
# n'avoir pas d'intérêt pour l'analyse