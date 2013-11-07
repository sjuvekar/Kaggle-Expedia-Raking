from single_column_features import SingleColumnFeatures

class VisitorAdrUsdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "visitor_hist_adr_usd", X)

  def derived_column_names(self):
    return ["visitor_hist_adr_usd_null", "visitor_hist_adr_usd_rank", "visitor_hist_adr_usd_percent", "visitor_hist_adr_usd_distance"]

  def derived_columns(self):
    return [self.isnull(), self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
