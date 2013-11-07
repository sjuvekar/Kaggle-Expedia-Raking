from single_column_features import SingleColumnFeatures

class PropLogHistoricalPriceFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_log_historical_price", X)

  def derived_column_names(self):
    return ["prop_log_historical_price_null", "prop_log_historical_price_rank", "prop_log_historical_price_percent", "prop_log_historical_price_distance"] 

  def derived_columns(self):
    return [self.column == 0, self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
