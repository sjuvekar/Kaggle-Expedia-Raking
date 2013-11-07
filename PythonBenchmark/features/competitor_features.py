from multi_column_features import MultiColumnFeatures

class CompetitorFeatures(MultiColumnFeatures):

  def __init__(self, X):
    col_names = map(lambda i: "comp{0}_rate".format(i), range(1, 9))
    MultiColumnFeatures.__init__(self, col_names, X)
    
  def derived_column_names(self):
    return ["competitor_total_nulls"]

  def derived_columns(self):
    return [self.count_nulls()]
