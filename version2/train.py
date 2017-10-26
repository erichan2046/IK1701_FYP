# Import necessary modules
import numpy as np
import pandas as pd
import data_handler as dh
from sklearn.svm import SVC
from sklearn.metrics import (brier_score_loss, precision_score, recall_score,
                             f1_score,accuracy_score,confusion_matrix,classification_report)
from sklearn import datasets, neighbors, linear_model
<<<<<<< HEAD
from sklearn.linear_model import LogisticRegression
=======
#from sklearn.linear_model import LogisticRegression
>>>>>>> e5f5640548555d9c1903d961ee9fd5433d7a1fc5
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import csv

topn_headlines = 20 # Select top 1 to topn_headlines as samples
train_sample_perc = .75 # The ratio of traning samples to the whole dataset

# Read the csv file
df_news = pd.read_csv("../stocknews/Combined_News_DJIA.csv")

# Convert the news matrix into sentiment score matrix
# with a column of sentiment sum scores
dataframe_col = 'Sum_sent' + str(topn_headlines)
df_news[dataframe_col] = 0
for i in range(1, topn_headlines+1):
	read_col = 'Top' + str(i)
	write_col = 'Top' + str(i) + '_sent'
	df_news[write_col] = np.array([dh.analize_sentiment(headline) for headline in df_news[read_col]])
	df_news[dataframe_col] = df_news[dataframe_col] + df_news[write_col]

# Extract feature set and label set
headlines_columns = range(1, topn_headlines+1)
X_data_list = [] # The feature set
for row in range(len(df_news)):
	X_data_row = []
	for i in range(1, topn_headlines+1):
		X_data_row.append(df_news.ix[row, 'Top'+str(i)+'_sent'])
	#X_data_row.append(df_news.ix[row, dataframe_col]) # Add sum_sent as a feature
	X_data_list.append(X_data_row)
Y_label = [] # The label set
for row in range(len(df_news)):
	Y_label.append(df_news.ix[row,'Label'])

# Break the dataset into training and testing sets
num_samples = len(df_news)
X_train = X_data_list[:int(num_samples * train_sample_perc)]
Y_train = Y_label[:int(num_samples * train_sample_perc)]
X_test = X_data_list[int(num_samples * train_sample_perc):]
Y_test = Y_label[int(num_samples * train_sample_perc):]

# Write the training set into a csv file
csvfile = file('../stocknews/train.csv','wb')
writer = csv.writer(csvfile)
header = ['No.']
for i in range(1, topn_headlines+1):
	header.append('Top'+str(i)+'_sent')
#header.append(dataframe_col) # Add sum_sent as a feature
header.append('Label')
writer.writerow(header)
for i in range(len(X_train)):
	writer.writerow([i+1]+X_train[i]+[int(Y_train[i])])
csvfile.close()

# Write the testing set into a csv file
csvfile = file('../stocknews/test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(header)
for j in range(len(X_test)):
	writer.writerow([j+1]+X_test[j]+[int(Y_test[j])])
csvfile.close()

# SVM for testing
# clf = SVC()
# clf.fit(X_train,Y_train)
# Y_predict = clf.predict(X_test)
# print(Y_predict)
# print(classification_report(Y_predict,Y_test))
# print('Accuracy: ' + str(clf.score(X_test, Y_test)))

# Build voting classifier for testing
<<<<<<< HEAD
logistic = LogisticRegression(random_state=1)
=======
#logistic = LogisticRegression(random_state=1)
>>>>>>> e5f5640548555d9c1903d961ee9fd5433d7a1fc5
rf = RandomForestClassifier(random_state=1)
gnb = GaussianNB()
svm = SVC(random_state=1,probability=True)

<<<<<<< HEAD
eclf1 = VotingClassifier(estimators=[('lr', logistic),('gnb',gnb),('svm',svm)],
						 voting='soft', weights=[1,1,1])
=======
eclf1 = VotingClassifier(estimators=[
      ('rf', rf),('gnb',gnb),('svm',svm)], voting='soft', weights=[1,1,1],
       flatten_transform=True)
>>>>>>> e5f5640548555d9c1903d961ee9fd5433d7a1fc5
eclf1 = eclf1.fit(X_train, Y_train)
Y_predict_vote = eclf1.predict(X_test)
print (classification_report(Y_predict_vote,Y_test))
print ("Accuracy: " + str(accuracy_score(Y_predict_vote, Y_test)))