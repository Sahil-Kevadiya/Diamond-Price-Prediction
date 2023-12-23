# Diamond-Price-Prediction

<h2>Importing Libraries:</h2>

The code starts by importing necessary libraries such as pandas, numpy, seaborn, and matplotlib for data manipulation, numerical operations, visualization, and plotting.
The warnings library is imported to handle warning messages.
There's a commented-out import statement (#import pandas.util.testing as tm) that seems to be unnecessary and can be removed.

<h2>Loading Data:</h2>

The pd.read_csv function is used to load a CSV file ("diamonds.csv") into a Pandas DataFrame named data.
The data is displayed using data.

<h2>Data Exploration:</h2>

data.info() is used to display information about the DataFrame, including data types and null values.
data.describe() provides summary statistics of the numerical columns.
Some columns (depth, table, x, y, z) are dropped from the DataFrame using data.drop.
The first few rows of the modified DataFrame are displayed using data.head().

<h2>Data Visualization:</h2>

Various histograms are plotted using Matplotlib to visualize the distributions of carat weight and diamond prices.
LabelEncoder from scikit-learn is used to convert categorical data ('cut' and 'clarity') into numeric form.
The 'color' column is mapped to numeric values using a dictionary.
Missing values in the 'color' column are filled with 0.
The target variable 'price' is converted to a float type.

<h2>Train-Test Split:</h2>

The data is split into training and testing sets using train_test_split from scikit-learn.

<h2>Feature Scaling:</h2>

StandardScaler is used to standardize the features by removing the mean and scaling to unit variance.

<h2>Model Building:</h2>

The code builds several regression models:
Linear Regression (LinearRegression)
Decision Tree Regressor (DecisionTreeRegressor)
Random Forest Regressor (RandomForestRegressor)
K-Neighbors Regressor (KNeighborsRegressor)
Lasso Regression (Lasso)
Ridge Regression (Ridge)
Each model is fitted on the training data, and predictions are made on the test data.
R-squared scores are calculated for each model and printed.

<h2>Prediction Function:</h2>

A function named prediction is defined to take user input for carat, cut, clarity, and color and predict the diamond price using the Random Forest model.

<h2>Model Serialization:</h2>

The Random Forest model (rf) is serialized using pickle and saved as a binary file named 'model1.pkl'.
<h2>Print Model Scores:</h2>

The R-squared scores of each model are printed at the end of the code.
