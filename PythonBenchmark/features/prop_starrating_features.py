from single_column_features import SingleColumnFeatures

class PropStarratingFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_starrating", X)

  def derived_column_names(self):
    return ["prop_starrating_null", "prop_starrating_rank", "prop_starrating_percent", "prop_starrating_distance"] 

  def derived_columns(self):
    return [self.column == 0, self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
