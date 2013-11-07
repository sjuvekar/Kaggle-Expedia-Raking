from single_column_features import SingleColumnFeatures

class VisitorLocationIdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "visitor_location_country_id", X)

  def derived_column_names(self):
    return ["visitor_id_ranks", "visitor_id_percent", "visitor_id_distance"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
