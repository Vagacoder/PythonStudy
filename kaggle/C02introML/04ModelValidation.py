#
# * Kaggle Course 02, Intro to Machine Learning
# * Model Validation

# * You'd first need to summarize the model quality into an understandable way. 
# * And it is better to be single metrics.

# * There are many metrics for summarizing model quality, but we'll start with 
# ! one called Mean Absolute Error (also called MAE).

# * Break down this metric:
# * (1) starting with the last word, error.
# * The prediction error for each predict is:

# ?    error=actual−predicted

# * (2) for A(bsolute)
# * Take the absolute value of each error, converting each error to a positive number.

# * (3) for M(ean)
# * Take the average of those absolute errors.

# * Summary for MAE: On average, our predictions are off by about X.

#%%
# * Read the data 
import pandas as pd

melbourne_file_path = '../data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
filtered_melbourne_data = melbourne_data.dropna(axis=0)
filtered_melbourne_data.head()

# %%
# * choose target and features
y = filtered_melbourne_data.Price

melbourne_features = [
    'Rooms',
    'Bathroom',
    'Landsize',
    'BuildingArea',
    'YearBuilt',
    'Lattitude',
    'Longtitude'
]

X = filtered_melbourne_data[melbourne_features]

print('y:', y.head(), sep='\n')
print('X:', X.head(), sep='\n')


# %%
# * Define the model
from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor()

# %%
# * fit the model
melbourne_model.fit(X, y)

# %%
# * predict on X
# ! However, this is bad practice, fit and predict using same set data
from sklearn.metrics import mean_absolute_error

predict_prices = melbourne_model.predict(X)
print(predict_prices)
mean_absolute_error(y, predict_prices)

# %%
# * split a part of data for validation
from sklearn.model_selection import train_test_split 

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1234)
# %%
# * re-define the model and fit it with split datasets
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

# %%
# * Now predict on validation datasets, see the HUGE difference between train set and vali set
val_predicts = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predicts))

# %%
