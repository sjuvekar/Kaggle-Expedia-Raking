from single_column_features import SingleColumnFeatures

class SrchBookingWindowFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "srch_booking_window", X)

  def derived_column_names(self):
    return ["srch_booking_window_rank", "srch_booking_window_percent", "srch_booking_window_distance"]

  def derived_columns(self):
    return [self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
