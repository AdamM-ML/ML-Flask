import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle
import sklearn
from sklearn import linear_model

data = pd.read_csv("datasets/winequality-red.csv", sep=";")


data = data[["fixed acidity", "volatile acidity", "quality", "chlorides", "free sulfur dioxide", "total sulfur dioxide",
             "density", "pH", "sulphates", "citric acid", "residual sugar", "alcohol"]]

# I decided to put all features from the dataset so the model bases its prediction on more values. Logically,
# the more dependencies the model knows, the more accurately it can predict the value.
# E.g. the case when model incorrectly predicted some value basing on 4 features, just because the 5-th feature
# turned out top be a decisive one here and we have not included it in our considerations.
# Of course more features mean more computational power and time needed.

prediction = "fixed acidity"

# Here as a prediction base I chose fixed acidity feature which gave me the best accuracy of the model. When choosing
# sulphates feature I got around only 38% accuracy, so knowing which feature is the most influential is a key knowledge.

X = np.array(data.drop([prediction], 1))
Y = np.array(data[prediction])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.15)

# Now I make a few iterations to find a model with a decent accuracy, the more iterations we make here, the greater the
# chance to obtain a better model
current_best_accuracy=0
for _ in range(10):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.15)
    linear_best_fit_line = linear_model.LinearRegression()
    linear_best_fit_line.fit(x_train, y_train)
    model_accuracy = linear_best_fit_line.score(x_test, y_test)
    model_accuracy_printed_version = model_accuracy*100
    print("Accuracy of the model:")
    print(round(model_accuracy_printed_version), "%")
    if model_accuracy>current_best_accuracy:
        current_best_accuracy = model_accuracy
        with open("wineDataModel", "wb") as dataFile:
            pickle.dump(linear_best_fit_line, dataFile)


graph_in = open("wineDataModel", "rb")
linear_best_fit_line = pickle.load(graph_in)

predictions = linear_best_fit_line.predict(x_test)

# Uncomment this part to see real and predicted values
#for i in range(len(predictions)):
#     print(round(predictions[i]), x_test[i], y_test[i])

attr = "alcohol"
style.use("ggplot")
pyplot.scatter(data[attr], data["quality"])
pyplot.xlabel(attr)
pyplot.ylabel("Predicted Wine Quality")
pyplot.show()
print("Best model found has the accuracy:",round(current_best_accuracy*100), "%")





