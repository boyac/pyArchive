# Recipes 6

# image classifer using deep learning
# the advantage of using deep learning is
# we do not need to manually extract the features,
# instead we can use the raw pixles of the image features
# and the classifier will do the rest

from sklearn import metrics, cross_validation
import tensorflow as tf
from tensorflow.contrib import learn

def main(unused_argv):
# load dataset:
	iris = learn.datasets.load.datasets('iris')
	x_train, x_test, y_train, y_test = cross_validation.train_test_split(
		iris.data, iris.target, test_size=0.2, random_state=42)

	# build 3 layer DNN with 10, 20, 10 units respectively
	classifier = learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)

	# fit and predict
	classifier.fit(x_train, y_train, steps=200)
	score = metrics.accuracy_score(y_test, classifier.predict(x_test))
	print('Accuracy: {0:f}'.format(score)) 
