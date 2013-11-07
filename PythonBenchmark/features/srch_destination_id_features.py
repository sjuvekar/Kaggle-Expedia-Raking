from single_column_features import SingleColumnFeatures

class SrchDestinationIdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "srch_destination_id", X)

  def derived_column_names(self):
    return ["srch_destination_id_percent", "srch_destination_id_rank", "srch_destination_id_distance"]

  def derived_columns(self):
    return [ self.percent(), self.rank_by_frequency(), self.distance_from_mean()]
