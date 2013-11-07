from single_column_features import SingleColumnFeatures

class PropLocationScore2Features(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_location_score2", X)

  def derived_column_names(self):
    return [ "prop_location_score2_percent", "prop_location_score2_rank", "prop_location_score2_distance"] 

  def derived_columns(self):
    return [ self.percent(), self.rank_by_frequency(), self.distance_from_mean()]
