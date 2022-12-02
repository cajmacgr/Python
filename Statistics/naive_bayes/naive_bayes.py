#Naive Bayes spam filter by Caleb MacGregor
 
import numpy as np
import os

# ===================== ABOUT THE DATA ========================
# Inside the 'data' folder, the emails are separated into 'train' 
# and 'test' data. Each of these folders has nested 'spam' and 'ham'
# folders, each of which has a collection of emails as txt files.
# You will only use the emails in the 'train' folder to train your 
# classifier, and will evaluate on the 'test' folder.
        
# The emails we are using are a subset of the Enron Corpus,
# which is a set of real emails from employees at an energy
# company. The emails have a subject line and a body, both of
# which are 'tokenized' so that each unique word or bit of
# punctuation is separated by a space or newline. The starter
# code provides a function that takes a filename and returns a
# set of all of the distinct tokens in the file.
# =============================================================

class NaiveBayes():
    """
    This is a Naive Bayes spam filter, that learns word spam probabilities 
    from our pre-labeled training data and then predicts the label (ham or spam) 
    of a set of emails that it hasn't seen before.
    """
    def __init__(self):

        self.num_train_hams = 0
        self.num_train_spams = 0
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.HAM_LABEL = 'ham'
        self.SPAM_LABEL = 'spam'

    def load_data(self, path:str='data/'):

        assert set(os.listdir(path)) == set(['test', 'train'])
        assert set(os.listdir(os.path.join(path, 'test'))) == set(['ham', 'spam'])
        assert set(os.listdir(os.path.join(path, 'train'))) == set(['ham', 'spam'])

        train_hams, train_spams, test_hams, test_spams = [], [], [], []
        for filename in os.listdir(os.path.join(path, 'train', 'ham')):
            train_hams.append(os.path.join(path, 'train', 'ham', filename))
        for filename in os.listdir(os.path.join(path, 'train', 'spam')):
            train_spams.append(os.path.join(path, 'train', 'spam', filename))
        for filename in os.listdir(os.path.join(path, 'test', 'ham')):
            test_hams.append(os.path.join(path, 'test', 'ham', filename))
        for filename in os.listdir(os.path.join(path, 'test', 'spam')):
            test_spams.append(os.path.join(path, 'test', 'spam', filename))

        return train_hams, train_spams, test_hams, test_spams

    def word_set(self, filename:list):

        with open(filename, 'r') as f:
            text = f.read()[9:] # Ignoring 'Subject:'
            text = text.replace('\r', '')
            text = text.replace('\n', ' ')
            words = text.split(' ')
            return set(words)

    def fit(self, train_hams:list, train_spams:list):

        self.num_train_hams = len(train_hams) # num of ham files
        self.num_train_spams = len(train_spams) # num of spam files

        #LOOPS THROUGH HAM FILES
        for i in train_hams:
            S = self.word_set(i)
            #LOOPS THROUGH SET
            for j in S:
                #Add to dictionary if not present, else adds 1 to count
                self.word_counts_ham[j] = self.word_counts_ham.get(j, 1) + 1

        #LOOPS THROUGH SPAM FILES
        for x in train_spams:
            S = self.word_set(x)
            #LOOPS THROUGH SET
            for y in S:
                #Add to dictionary if not present, else adds 1 to count
                self.word_counts_spam[y] = self.word_counts_spam.get(y, 1) + 1

    def predict(self, filename:str):

        S = self.word_set(filename)
        tot_prob_spam = 0
        tot_prob_ham = 0

        #Probility of spam and ham emails
        p_spam = (self.num_train_spams) / (self.num_train_spams + self.num_train_hams)
        p_ham = (self.num_train_hams) / (self.num_train_spams + self.num_train_hams)
        
        #LOOP FOR SPAM
        for i in S:
            # (count + 1) / (total spams + 2)
            frac = (self.word_counts_spam.get(i, 0) + 1) / (self.num_train_spams + 2)
            # Total = sum of all log(frac)
            tot_prob_spam = tot_prob_spam + np.log(frac)
        # Total = Total + probability of spam email
        tot_prob_spam = np.log(p_spam) + tot_prob_spam

        #LOOP FOR HAM
        for j in S:
            # (count + 1) / (total hams + 2)
            frac = (self.word_counts_ham.get(j, 0) + 1) / (self.num_train_hams + 2)
            # Total = sum of all log(frac)
            tot_prob_ham = tot_prob_ham + np.log(frac)
        # Total = Total + probability of ham email
        tot_prob_ham = np.log(p_ham) + tot_prob_ham

        #Checks which probabilty is higher; in case of tie choose HAM
        if tot_prob_spam > tot_prob_ham:
            return self.SPAM_LABEL
        else:
            return self.HAM_LABEL
            

    def accuracy(self, hams:list, spams:list):

        total_correct = 0
        total_datapoints = len(hams) + len(spams)
        for filename in hams:
            if self.predict(filename) == self.HAM_LABEL:
                total_correct += 1
        for filename in spams:
            if self.predict(filename) == self.SPAM_LABEL:
                total_correct += 1
        return total_correct / total_datapoints

if __name__ == '__main__':
    # Create a Naive Bayes classifier.
    nbc = NaiveBayes()

    # Load all the train/test ham/spam data.
    train_hams, train_spams, test_hams, test_spams = nbc.load_data()

    # Fit the model to the training data.
    nbc.fit(train_hams, train_spams)

    # Print out the accuracy on the train and test sets.
    print("Train Accuracy: {}".format(nbc.accuracy(train_hams, train_spams)))
    print("Test  Accuracy: {}".format(nbc.accuracy(test_hams, test_spams)))
