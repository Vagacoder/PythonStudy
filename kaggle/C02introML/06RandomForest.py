#
# * Kaggle Course 02, Intro to Machine Learning
# * Random Forest

# ! Problem of Decision Tree
# * Too many leaves causes overfitting, because of decisions at deep of tree is
# *     made basing on a few samples
# * Too few leaves causes underfitting, because of decisions are made basing on
# *     large amount of samples

# * Random forest using many trees, prediction is made by averaging the prediction
# * of each component tree. 

# %%
# * Load data as 05
import pandas as pd
from sklearn.model_selection import train_test_split

melbourne_file_path = '../data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
filtered_mlb_data = melbourne_data.dropna(axis=0)

y = filtered_mlb_data.Price
melb_features = [
    'Rooms', 'Bathroom', 'Landsize',
    'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude'
]

X = filtered_mlb_data[melb_features]

train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=123)

# %%
# * Build Random Forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forestModel = RandomForestRegressor(random_state=123)
forestModel.fit(train_X, train_y)
melb_pred = forestModel.predict(val_X)
print(mean_absolute_error(melb_pred, val_y))

# %%
