# write our classifier from scratch
import random 
from scipy.spatial import distance

def euc(a,b): 
	# a is a point from our training data, b is a point from our testing data
	# below function returns the distance between them 
	return distance.euclidean(a,b) 

class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self, X_test):
		# this ouputs the prediction of the labels
		predictions = []
		for row in X_test:
			# label = random.choice(self.y_train)
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		# calculating the distance from our test to the training point
		best_dist = euc(row, self.X_train[0]) # keep track of the shortest training point
		best_index = 0 # keep track of the index
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index]


from sklearn import datasets 
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
#my_classifier = KNeighborsClassifier()
my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train) # fit does the training

predictions = my_classifier.predict(X_test) # predict does the prediction

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

# summary:
# nearest neighbor classifer is easy to implement
# but it's slow since it needs to iterate over each point to find the closest
# also it is hard to represent relationship between feattures
# since some features are more representative from others
