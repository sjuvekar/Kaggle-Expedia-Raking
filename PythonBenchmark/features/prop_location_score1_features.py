from single_column_features import SingleColumnFeatures

class PropLocationScore1Features(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_location_score1", X)

  def derived_column_names(self):
    return ["prop_location_score1_rank", "prop_location_score1_percent", "prop_location_score1_distance"] 

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
