from single_column_features import SingleColumnFeatures

class PropIdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_id", X)

  def derived_column_names(self):
    return ["prop_id_percent", "prop_id_rank", "prod_id_distance"]

  def derived_columns(self):
    return [self.percent(), self.rank_by_frequency(), self.distance_from_mean()]
