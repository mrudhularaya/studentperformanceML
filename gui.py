import tkinter as tk
import pickle
import sklearn
from sklearn import linear_model
import pandas as pd
import numpy as np

HEIGHT = 750
WIDTH = 750

root = tk.Tk()

root.title("Student Performance")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#fff')
canvas.pack()

frame = tk.Frame(canvas, bg='#0F212E')
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

frame2 = tk.Frame(canvas, bg='#0F212E')
frame2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.9)

z = tk.StringVar()


def submit():
    filename = z.get()
    entrybox.delete(0, tk.END)
    ogdata = pd.read_csv(filename, sep=",")

    # Select required attributes
    data = ogdata[['G1', 'G2', 'absences', 'failures', 'Fedu']]

    # define name
    name = list(ogdata['Name'])

    # Specify X and y
    X = np.array(data)

    # Load the model
    pickle_in = open("studentmodel.pickle", "rb")
    linear = pickle.load(pickle_in)

    # Make predictions
    predictions = linear.predict(X)

    # Define remedial
    fail = 10
    remedial = 'Marks: \n\n'
    remedialnames = "Name: \n\n"
    for i in range(len(predictions)):
        if predictions[i] < fail:
            remedialnames += str(name[i]) + "\n"
            remedial += str(predictions[i]) + "\n"

    label2 = tk.Label(frame2, text="Remedial students are: ", bg="#0F212E", fg="#fff")
    label2.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.05)

    label3 = tk.Label(frame2, text=remedialnames, bg="#0F212E", fg="#fff")
    label3.place(relx=0.01, rely=0.07, relwidth=0.4, relheight=0.9)

    label4 = tk.Label(frame2, text=remedial, bg="#0F212E", fg="#fff")
    label4.place(relx=0.52, rely=0.07, relwidth=0.4, relheight=0.9)


label = tk.Label(frame, text="Enter the file name : ", bg="#0F212E", fg="#FCFBF7")
label.place(relx=0, rely=0.28, relwidth=0.3, relheight=0.2)
label.config(font=("Proxima Nova", 11))

entrybox = tk.Entry(frame, bg="#A9A9AC", textvariable=z)
entrybox.place(relx=0.3, rely=0.28, relwidth=0.4, relheight=0.2)
entrybox.config(font=("Roboto", 10))

button = tk.Button(frame, text="Submit", bg="#A9A9AC", command=submit)
button.place(relx=0.75, rely=0.28, relwidth=0.2, relheight=0.23)
button.config(font=("Roboto", 10))

root.mainloop()
