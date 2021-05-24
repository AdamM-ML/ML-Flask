import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier

wineData = datasets.load_wine()

x = wineData.data
y = wineData.target
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.25)
types = ["class_0", "class_1", "class_2"]

# Choosing 'linear' kernel here in order not to wait very long time to run the code. This choice determines how accurate
#the model is. Changing the value of 'C' changes the soft margin scope and this change can also influence the
#accuracy value

classifier = svm.SVC(kernel="linear", C=2)
classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)
model_accuracy = metrics.accuracy_score(y_test, prediction)
print("Model's accuracy (SVM):", round(model_accuracy*100), "%")

# Predicting with linear regression and KNN models to compare accuracies

linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(x_train, y_train)
linear_regression_model_accuracy = linear_regression_model.score(x_test, y_test)
print("Model's accuracy (linear regression):", round(linear_regression_model_accuracy*100), "%")

classifier = KNeighborsClassifier(n_neighbors=7) # Replacing the SVM classifier with KNN classifier
classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)
model_accuracy = metrics.accuracy_score(y_test, prediction)
print("Model's accuracy (KNN):", round(model_accuracy*100), "%")
