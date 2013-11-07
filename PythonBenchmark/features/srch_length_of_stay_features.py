from single_column_features import SingleColumnFeatures

class SrchLengthOfStayFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "srch_length_of_stay", X)

  def derived_column_names(self):
    return ["srch_length_rank", "srch_length_percent", "srch_length_distance"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
