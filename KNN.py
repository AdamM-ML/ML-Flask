import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("zoo.data")

preproc_data = preprocessing.LabelEncoder()
#animal_name = preproc_data.fit_transform(list(data["animal_name"]))
hair = preproc_data.fit_transform(list(data["hair"]))
feathers = preproc_data.fit_transform(list(data["feathers"]))
eggs = preproc_data.fit_transform(list(data["eggs"]))
milk = preproc_data.fit_transform(list(data["milk"]))
airborne = preproc_data.fit_transform(list(data["airborne"]))
predator = preproc_data.fit_transform(list(data["predator"]))
toothed = preproc_data.fit_transform(list(data["toothed"]))
backbone = preproc_data.fit_transform(list(data["backbone"]))
breathes = preproc_data.fit_transform(list(data["breathes"]))
venomous = preproc_data.fit_transform(list(data["venomous"]))
aquatic = preproc_data.fit_transform(list(data["aquatic"]))
fins = preproc_data.fit_transform(list(data["fins"]))
legs = preproc_data.fit_transform(list(data["legs"]))
tail = preproc_data.fit_transform(list(data["tail"]))
domestic = preproc_data.fit_transform(list(data["domestic"]))
catsize = preproc_data.fit_transform(list(data["catsize"]))
type = preproc_data.fit_transform(list(data["type"]))

predict = "type"

X = list(zip(hair,feathers,eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,venomous,fins,
             legs,tail,domestic,catsize,type))
Y= list(type)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.20)

k = 9
'''
for _ in range(3):
    k = k+2
    KNN_model = KNeighborsClassifier(n_neighbors=k) #acc depends on this mainly
    KNN_model.fit(x_train, y_train)
    model_accuracy = KNN_model.score(x_test, y_test)
    print("Accuracy (k=",k,"):")
    print(round(model_accuracy*100),"%")
'''

KNN_model = KNeighborsClassifier(n_neighbors=k) #acc depends on this mainly
KNN_model.fit(x_train, y_train)
model_accuracy = KNN_model.score(x_test, y_test)
print("Accuracy (k=",k,"):")
print(round(model_accuracy*100),"%")
predicted = KNN_model.predict(x_test)

data_names = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(predicted)):
    print("Predicted class:", data_names[predicted[i]], "For data:", x_test[i], "Original class:", data_names[y_test[
        i]], "Considered neighbours:", KNN_model.kneighbors([x_test[i]], n_neighbors=3))

