import pandas

class MultiColumnFeatures(object):
	
	def __init__(self, names, X, verbose=1):
		self.names = names
		self.columns = X[names]
		self.verbose = verbose

	def derived_column_names(self):
		pass

	def derived_columns(self):
		pass

	def features(self):
		if (self.verbose):
			print "Creating " + self.__class__.__name__
		return pandas.concat(self.derived_columns(), axis = 1, keys=self.derived_column_names())

	def count_nulls(self):
		return pandas.isnull(self.columns).sum(axis=1)
