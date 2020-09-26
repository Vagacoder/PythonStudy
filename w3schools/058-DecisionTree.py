#
# * Decision tree

#%%
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg

df = pandas.read_csv('data/shows.csv')

print(df)

# %%
# * Convert to Numerical Data
# * Decision Tree need all data numerical
# * convert columns 'Nationality' and 'GO' into numerical values
dic = {'UK':0, 'USA':1, 'N':2}
df['Nationality'] = df['Nationality'].map(dic)
dic = {'YES':1, 'NO':0}
df['Go'] =df['Go'].map(dic)

print(df)
# %%
# * Go is targe column, need be separated from other feature columns
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)
# %%
# * Create decision tree
dtree = DecisionTreeClassifier().fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('data/mydecisiontree.png')

img=pltimg.imread('data/mydecisiontree.png')
imgplot= plt.imshow(img)
plt.show()

# %%
# * Predicte
print(dtree.predict([[40, 10, 7, 1]]))
print("[1] means 'GO'")
print("[0] means 'NO'")
# %%
