import pandas
import random
import data_io

def train_test_sample(features):
  # Initalize the index araay to all False
  train_index_array = [False] * len(features)
  test_index_array = [False] * len(features)

  # Initialize random number generator
  random.seed(1)
  random_seed = random.random()    

  # Initalize the current search id
  curr_srch_id = -1

  # This dictionary keeps track of all positions being held
  position_dict = dict()

  for i in range(len(features)):
    srch_id = features["srch_id"][i]
    # If new search query, clear the dictionary
    if srch_id != curr_srch_id:
      curr_srch_id = srch_id
      # Pick one guy from each position randomly
      for v in position_dict.values():
        picked_id = random.sample(v, 1)[0]
        if random_seed > 0.75:
          test_index_array[picked_id] = True
        else:
          train_index_array[picked_id] = True
      position_dict.clear()
      random_seed = random.random()    

    # Include all clicked/bookied items
    if features["booking_bool"][i] == 1 or features["click_bool"][i] == 1:
      if random_seed > 0.75:
        test_index_array[i] = True
      else:
        train_index_array[i] = True
      continue
  
    # Find scaled position from 1 to 5
    raw_position = features["position"][i]
    position = raw_position / 10 + 1
    if position in position_dict.keys():
      position_dict[position] = position_dict[position] + [i]
    else:
      position_dict[position] = [i]

  # Done. We have a sample
  print sum(train_index_array)
  print sum(test_index_array)
  return (train_index_array, test_index_array)


if __name__ == "__main__":
  print("Reading training data")
  train_chunks = data_io.read_train_features()
  train = pandas.concat([chunk for chunk in train_chunks], ignore_index=True)

  (train_sample_ids, test_sample_ids) = train_test_sample(train)
  
  # Create Train and Test
  trainX = train[train_sample_ids]
  testX = train[test_sample_ids]

  print "Train: ", len(trainX)
  print "Test: ", len(testX)

  data_io.save_train_test_split( (trainX, testX) )
