ESILV A4 - Python for data analysis project
==

On this repository you will find the work of ROUET Thibaut and RICHARD Raphaël around the dataset [Diabetes 130-US hospitals for years 1999-2008 Data Set](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)

We had to analyze this dataset and produce a Python code containing some Data Visualization allowing us to study the possibility for a patient to be readmitted in the hospital under 30 days after leaving it.
In this Python code, we also had to try to predict if a patient would be readmitted based on the other elements of the Dataset, using different models of Machine Learning.

After doing it, we concluded that this dataset really was enormous, as even after deleting 40% of the informations that were not pertinent for our study, it was still too big for the OneHotEncoder function to work and the GridSearch function had to take too many hours to work so we couldn't make it function.
However, we still managed to get almost 90% of accuracy in our predictions using the RandomForest and Support Vector functions, which proves that what we did was still pretty efficient
