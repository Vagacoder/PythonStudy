#
# * Kaggle Course 02, Intro to Machine Learning
# * Underfitting and Overfitting

#%%
# * Import libs
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

#%%
# * define function
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state = 123)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

#%%
# * Data Loading Code
import pandas as pd 

melbourne_file_path ='../data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

filtered_melbourne_data = melbourne_data.dropna(axis=0)

filtered_melbourne_data.head()

#%%
# * define datasets
y = filtered_melbourne_data.Price

melbourne_features = [
    'Rooms', 'Bathroom', 'Landsize', 'BuildingArea',
    'YearBuilt', 'Lattitude', 'Longtitude'
]

X = filtered_melbourne_data[melbourne_features]

#%%
# * Split to train and validation data
from sklearn.model_selection import train_test_split 

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=123)

#%%
# * Compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print('Max lead nodes: %d \t\t Mean Absolute Error: %d' \
        %(max_leaf_nodes, my_mae))

# %%
