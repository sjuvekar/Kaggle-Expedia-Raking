import data_io
import numpy
import pandas
import random
import sample
from feature_extractor import FeatureExtractor
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.cross_validation import train_test_split

def objective(cols, whichClassifier):
  if whichClassifier == "five":
    if cols["booking_bool"] == 1:
      return 1
    else:
      return 0

  elif whichClassifier == "one":
    if cols["click_bool"] == 1 and cols["booking_bool"] != 1:
      return 1
    else:
      return 0

  else:
    if cols["booking_bool"] == 1 or cols["click_bool"] == 1:
      return 0
    else:
      return 1


def classify(train, train_sample_ids, test_sample_ids, whichClassifier):
  feature_names = list(train.columns)
  feature_names.remove("click_bool")
  feature_names.remove("booking_bool")
  feature_names.remove("gross_bookings_usd")
  #feature_names.remove("date_time")
  feature_names.remove("position")

  # Create Train and Test
  trainX = train[feature_names][train_sample_ids]
  testX = train[feature_names][test_sample_ids]
  Y_columns = ["click_bool", "booking_bool", "position"]
  trainY = train[Y_columns][train_sample_ids].apply(lambda x: objective(x, whichClassifier), axis=1)
  testY = train[Y_columns][test_sample_ids].apply(lambda x: objective(x, whichClassifier), axis=1)

  print "Train: ", len(trainY)
  print "Test: ", len(testY)

  print("Training the Classifier")
  classifier = GradientBoostingClassifier(n_estimators=1024, 
                                          verbose=3,
                                          subsample=0.8,
                                          min_samples_split=10,
                                          max_depth = 6,
                                          random_state=1)
  classifier.fit(trainX, trainY)
    
  print "Score = ", classifier.score(testX, testY)

  return classifier


def main():
    print("Reading training data")
    train_chunks = data_io.read_train_features()
    train = pandas.concat([chunk for chunk in train_chunks], ignore_index=True)
    
    print("Sampling")
    (train_sample_ids, test_sample_ids) = sample.train_test_sample(train)
    
    print("Training five Classifier")
    fiveClassifier = classify(train, train_sample_ids, test_sample_ids, "five")

    print("Training one Classifier")
    oneClassifier = classify(train, train_sample_ids, test_sample_ids, "one")

    print("Training zero Classifier")
    zeroClassifier = classify(train, train_sample_ids, test_sample_ids, "zero")

    classifier = (fiveClassifier, oneClassifier, zeroClassifier)
    
    print("Saving the classifiers")
    data_io.save_model(classifier)

    
if __name__=="__main__":
    main()
