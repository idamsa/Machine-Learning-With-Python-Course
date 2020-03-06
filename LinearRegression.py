import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# trains 30 models and saves only the best one
best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)

    linear = linear_model.LinearRegression()

# train model
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test) # accuracy
    print(acc)

# save model if acc grater than best we've seen before
    if acc > best:
        best = acc
        with open("studentmodel.pickle","wb") as f:
            pickle.dump(linear, f)

# Load saved model
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# print the coefficient and the intercept for the model
print("Coeficient: " , linear.coef_)
print("Intercept: " , linear.intercept_)

# predict on the test set
predictions = linear.predict(x_test)

# prints actual values and the predicted value
for x in range(len(predictions)) :
    print(predictions[x], x_test[x], y_test[x])

# Plotting the data 
p = "failures"  # x value for plotting
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()




