# pipeline for SVL
# SPAM classifier
# email/label; partition our data into train/test

# import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data #input, features
y = iris.target #output, labels

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5) # 150 data in iris 75 in train, 75 in test


# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()
# import classifier/prediction model
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

# train our classifier using the training data
my_classifier.fit(X_train, y_train) 
# then now the classifier is ready to be use to classify data
# classify our testing data
predictions = my_classifier.predict(X_test)
print predictions

# see how accuracy the prediction is
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions) #predicted label/true label


# keypoint
'''
my_classifier.fit(X_train, y_train);
we use train data to train the classifier.
and we use:
my_classifier.predict(X_test)
test data to see how accurate it is
'''
