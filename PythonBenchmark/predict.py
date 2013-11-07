import data_io
import pandas
import numpy
from feature_extractor import FeatureExtractor

def class_probabilities(features, classifiers):
    fiveClassifier = classifiers[0]
    oneClassifier = classifiers[1]
    zeroClassifier = classifiers[2]

    print("Making predictions using fiveClassifier")
    five = fiveClassifier.predict_proba(features)

    print("Making predictions using oneClassifier")
    one = oneClassifier.predict_proba(features)

    print("Making predictions using zeroClassifier")
    zero = zeroClassifier.predict_proba(features)

    class_labels = numpy.array([0, 1, 5])
    
    # Every probability is computed as an average of two probabilities:
    # e.g. p(class = 0) = avg(zero[:, 1], (one[:, 0] + five[:, 0]))
    # Don't forget to normalize probabilities
    sum = (zero[:, 0] + one[:, 0] + five[:, 0])
    class_zero = (sum - zero[:, 0]) * class_labels[0] 
    print class_zero
    class_one = (sum - one[:, 0]) * class_labels[1] 
    print class_one
    class_five = (sum - five[:, 0]) * class_labels[2] 
    print class_five
    den = 2 * sum 
    return (class_zero + class_one + class_five) / den
 
def main():
    print("Reading test data")
    test_chunks = data_io.read_test_features()
    test = pandas.concat([chunk for chunk in test_chunks], ignore_index=True)

    feature_names = list(test.columns)
    #feature_names.remove("date_time")

    features = test[feature_names].values

    print("Loading the classifier")
    classifiers = data_io.load_model()

    print("Making predictions")
    #orig_predictions = classifier.predict_proba(features)
    #multiplier = 2 ** classifier.classes_ 
    #predictions = orig_predictions * multiplier
    #predictions = predictions.sum(axis=1)
    predictions = class_probabilities(features, classifiers)
    print predictions
    predictions = list(-1.0*predictions)
    recommendations = zip(test["srch_id"], test["prop_id"], predictions)

    print("Writing predictions to file")
    data_io.write_submission(recommendations)

if __name__=="__main__":
    main()
