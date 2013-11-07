from single_column_features import SingleColumnFeatures

def __sane__price__(x):
  if x > 10000:
    return 2
  if x > 1000:
    return 1
  return 0

class PriceUsdFeatures(SingleColumnFeatures):

  def __init__(self, X):
    SingleColumnFeatures.__init__(self, "price_usd", X)

  def derived_column_names(self):
    return ["price_usd_sane"]

  def derived_columns(self):
    return [ self.column.map(__sane__price__) ]
