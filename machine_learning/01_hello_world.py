# Recipes 1 - Decision Tree/Classifier
from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] #[weight, (0/1) bummpy or not]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[150, 0]]) # 0 for apple, 1 for orange

