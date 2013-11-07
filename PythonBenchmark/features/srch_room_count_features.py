from single_column_features import SingleColumnFeatures

class SrchAdultCountFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "srch_adults_count", X)

  def derived_column_names(self):
    return ["srch_adult_count_rank", "srch_adult_count_percent"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent()]
