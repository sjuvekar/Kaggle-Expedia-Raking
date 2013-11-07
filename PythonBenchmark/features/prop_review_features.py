from single_column_features import SingleColumnFeatures

class PropReviewFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "prop_review_score", X)

  def derived_column_names(self):
    return ["prop_review_null", "prop_review_rank", "prop_review_percent", "prop_review_distance"] 

  def derived_columns(self):
    return [self.column == 0, self.rank_by_frequency(), self.percent(), self.distance_from_mean()]
