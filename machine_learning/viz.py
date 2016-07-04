# Recipes 2 - Iris

# Goals
#- import dataset
#- train a classifier
#- predict label for new flower
#- visualize the tree 

from sklearn.datasets import load_iris

# step 1: import dataset
iris = load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]
for i in range(len(iris.target)): 
	# the target variable have 100 500 entries
	# iterate over them to print out the entire dataset
	print 'Example %d: label %s, features %s' % (i, iris.target[i], iris.data[i])


# step 2: testing data
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree # create a decision tree classfier
iris = load_iris()
test_idx = [0,50, 100]

# training data, containing majority of the data 
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data, just containing the data that had been removed
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)


# step 3: Predict label for new flower
print test_target
print clf.predict(test_data) # give the features of our test data and see how does te predition go


# step 4: viz
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, 
						out_file=dot_data,
						feature_names=iris.feature_names,
						class_names=iris.target_names,
						filled=True, rounded=True,
						impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')

print test_data[0], test_target[0]
print iris.feature_names, iris.target_names

# Choosing good features is one of your most important jobs
# Better features can build better trees

