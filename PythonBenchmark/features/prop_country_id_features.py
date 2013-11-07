from single_column_features import SingleColumnFeatures

class PropCountryIdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_country_id", X)

  def derived_column_names(self):
    return ["prop_country_id_rank", "prop_country_id_percent", "prop_country_id_distance"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
