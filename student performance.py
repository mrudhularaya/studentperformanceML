import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
import pickle

# Read the data
filename = str(input("Enter the csv file name: "))
ogdata = pd.read_csv(filename, sep=";")

# Select required attributes
data = ogdata[['G1', 'G2', 'G3', 'absences', 'failures', 'Fedu']]

# Specify Prediction
predict = 'G3'

# Specify X and y
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# Split the data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# Train to get the best model/highest accuracy
'''
best = 0
for _ in range(35):

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    # Define the linear regression model
    linear = linear_model.LinearRegression()

    # Fit the model to training set
    linear.fit(x_train, y_train)

    # Print accuracy
    acc = linear.score(x_test, y_test)
    print(acc)
    # Save the model
    if acc > best:
        print("best:", best)
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)'''

# Load the model
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# Make predictions
predictions = linear.predict(x_test)

# Print predictions
for i in range(len(predictions)):
    print(predictions[i], x_test[i], y_test[i])
'''
remedial = []
for i in range(len(predictions)):
    if predictions[i] < 10:
        remedial.append(predictions[i])

print("Remedial students are: ")
for i in range(len(remedial)):
    print(remedial[i])
'''