import csv
from operator import itemgetter
import os
import json
import pickle
import pandas as pd

def get_paths():
    paths = json.loads(open("SETTINGS.json").read())
    for key in paths:
        paths[key] = os.path.expandvars(paths[key])
    return paths

def read_train():
    train_path = get_paths()["train_path"]
    return pd.read_csv(train_path)

def read_test():
    test_path = get_paths()["test_path"]
    return pd.read_csv(test_path)

def read_train_features():
    feature_path = get_paths()["train_feature_path"]
    return pd.read_csv(feature_path, iterator=True, chunksize=10000)

def read_test_features():
    feature_path = get_paths()["test_feature_path"]
    return pd.read_csv(feature_path, iterator=True, chunksize=10000)

def save_train_features(features):
    features.as_csv(get_paths()["train_feature_path"])

def save_test_features(features):
    features.as_csv(get_paths()["test_feature_path"])

def save_train_test_split(train_test_split_arrays):
    with open(get_paths()["train_test_split_path"], "w") as output:
      pickle.dump(train_test_split_arrays, output)

def save_model(model):
    out_path = get_paths()["model_path"]
    pickle.dump(model, open(out_path, "w"))

def load_model():
    in_path = get_paths()["model_path"]
    return pickle.load(open(in_path))

def write_submission(recommendations, submission_file=None):
    if submission_file is None:
        submission_path = get_paths()["submission_path"]
    else:
        path, file_name = os.path.split(get_paths()["submission_path"])
        submission_path = os.path.join(path, submission_file)
    rows = [(srch_id, prop_id)
        for srch_id, prop_id, rank_float
        in sorted(recommendations, key=itemgetter(0,2))]
    writer = csv.writer(open(submission_path, "w"), lineterminator="\n")
    writer.writerow(("SearchId", "PropertyId"))
    writer.writerows(rows)
