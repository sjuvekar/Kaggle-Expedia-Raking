import data_io
import numpy
import pandas
import random
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

  #if cols["click_bool"] == 1:
  #  if whichClassifier == "lessThanZero":
  #    return 1
  #  else:
  #    return 0
  #if cols["position"] <= 10:
  #  return 3
  #if cols["position"] <= 20:
  #  return 2
  #if cols["position"] <= 30:
  #  return 1
  #return 0


def sample_train_index(train, whichClassifier):
    sample_idx = train.index[train["booking_bool"] == 1]
    sample_idx = sample_idx.union(train.index[train["click_bool"] == 1])
    if whichClassifier == "five":
        random.seed(1)
        sample_size = 200000
    elif whichClassifier == "one":
        random.seed(11)
        sample_size = 200000
    else:
        random.seed(111)
        sample_size = 200000
    idx_10 = train.index[(train["booking_bool"] == 0) & (train["click_bool"] == 0) & (train["position"] <= 10)]
    sample_idx = sample_idx.union(train.index[random.sample(idx_10, sample_size)])
    idx_20 = train.index[(train["booking_bool"] == 0) & (train["click_bool"] == 0) & (train["position"] > 10) & (train["position"] <= 20)]
    sample_idx = sample_idx.union(train.index[random.sample(idx_20, sample_size)])
    idx_30 = train.index[(train["booking_bool"] == 0) & (train["click_bool"] == 0) & (train["position"] > 20) & (train["position"] <= 30)]
    sample_idx = sample_idx.union(train.index[random.sample(idx_30, sample_size)])
    idx_40 = train.index[(train["booking_bool"] == 0) & (train["click_bool"] == 0) & (train["position"] > 30) & (train["position"] <= 40)]
    sample_idx = sample_idx.union(train.index[random.sample(idx_40, sample_size)])
  
    #random_idx = train.index[random.sample(train.index, 1000000)]
    #sample_idx = sample_idx.union(random_idx)
    return sample_idx


def split(train, features, target):
  train_dict = dict()

  random.seed(1)
  for i in train.index:
    id = train["srch_id"][i]
    try:
      x = train_dict[id]
      continue
    except:
      pass
    if train["booking_bool"][i] == 1:
      if random.uniform(0, 1) <= 0.85:
        train_dict[id] = 0

  print len(train_dict.keys())
  # train_dict is filled
  train_idx = features["srch_id"].apply(lambda a: a in train_dict.keys())
  test_idx = features["srch_id"].apply(lambda a: a not in train_dict.keys())

  # Finished collecting ids, create data
  trainX = features[train_idx]
  testX = features[test_idx]
  trainY = target[train_idx][0]
  testY = target[test_idx][0]
  print "Shapes = ", trainX.shape, testX.shape, trainY.shape, testY.shape
  return (trainX, testX, trainY, testY)


def classify(train, whichClassifier):
  train_sample = train.ix[sample_train_index(train, whichClassifier)]
  print "Len: ", train_sample.shape

  feature_names = list(train.columns)
  feature_names.remove("click_bool")
  feature_names.remove("booking_bool")
  feature_names.remove("gross_bookings_usd")
  #feature_names.remove("date_time")
  feature_names.remove("position")

  features = train_sample[feature_names]
  
  target = train_sample[["click_bool", "booking_bool", "position"]].apply(lambda x: objective(x, whichClassifier), axis=1)
  print "Positive: ", numpy.sum(target) 
  target = pandas.DataFrame(target, index = features.index)

  print("Train-Test split")
  trainX, testX, trainY, testY = split(train_sample, features, target) #train_test_split(features, target, random_state = 1)

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
    
    print("Training five Classifier")
    fiveClassifier = classify(train, "five")

    print("Training one Classifier")
    oneClassifier = classify(train, "one")

    print("Training zero Classifier")
    zeroClassifier = classify(train, "zero")

    classifier = (fiveClassifier, oneClassifier, zeroClassifier)
    
    print("Saving the classifiers")
    data_io.save_model(classifier)

    
if __name__=="__main__":
    main()
