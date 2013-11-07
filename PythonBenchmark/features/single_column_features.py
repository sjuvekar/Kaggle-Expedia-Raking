import pandas
from scipy import stats

# Helper functions
def __percent_of__(value_count_dict, value_count_sum, new_value):
	try:
		return float(value_count_dict[new_value]) / value_count_sum
	except:
		return 0


# value_count_index has to be sorted by frequency
def __rank_of__(value_count_index, new_value):
	try:
		return value_count_index.index(new_value)
	except:
		return -1

# Distance of current value from mean in multiples of stddev
def __distance_of__(value, mean, std):
	if numpy.isnan(value):
		return -1
	else:
		return float(abs(value - mean)) / float(std)


class SingleColumnFeatures(object):
	
	def __init__(self, name, X, verbose=1):
		self.name = name
		self.column = X[name]
		self.verbose = verbose


	def derived_column_names(self):
		pass

	def derived_columns(self):
		pass

	def features(self):
		if (self.verbose):
			print "Creating " + self.__class__.__name__
		return pandas.concat(self.derived_columns(), axis = 1, keys=self.derived_column_names())

	def isnull(self):
		return self.column.isnull()

	def percent(self):
		value_count_table = self.column.value_counts()
		value_count_sum = value_count_table.sum()
		return self.column.apply(lambda x: __percent_of__(value_count_table, value_count_sum, x))

	def rank_by_frequency(self):
		value_count_table = self.column.value_counts()
		value_count_index = list(value_count_table.index)
		return self.column.apply(lambda x: __rank_of__(value_count_index, x))

	def rank_by_quantity(self):
		value_count_table = self.column.value_counts()
		value_count_index = sorted(value_count_table.keys())
		return self.column.apply(lambda x: __rank_of__(value_count_index, x))

	def distance_from_mean(self):
		mean = stats.nanmean(self.column)
		std = stats.nanstd(self.column)
		return self.column.apply(lambda x: __distance_of__(x, mean, std))
