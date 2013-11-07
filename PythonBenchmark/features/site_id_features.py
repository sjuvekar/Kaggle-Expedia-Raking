from single_column_features import SingleColumnFeatures

class SiteIdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "site_id", X)
    
  def derived_column_names(self):
    return ["site_id_ranks", "site_id_percent", "site_id_distance"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
