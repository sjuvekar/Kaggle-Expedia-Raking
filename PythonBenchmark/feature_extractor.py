import argparse
import pandas
import data_io
import multiprocessing

from features import *

G_PROCESS_POOL = multiprocessing.Pool()

class FeatureExtractor:
    def __init__(self, X):
      self.X = X
      print "Data Size = ", self.X.shape

    def transformer(self, fet):
      return fet.features()

    def feature_extractor(self):
      feature_list = [
          site_id_features.SiteIdFeatures(self.X),
          visitor_location_id_features.VisitorLocationIdFeatures(self.X),
          visitor_starrating_features.VisitorStarratingFeatures(self.X),
          visitor_adr_usd_features.VisitorAdrUsdFeatures(self.X),
          prop_country_id_features.PropCountryIdFeatures(self.X),
          prop_id_features.PropIdFeatures(self.X),
          prop_starrating_features.PropStarratingFeatures(self.X),
          prop_review_features.PropReviewFeatures(self.X),
          prop_location_score1_features.PropLocationScore1Features(self.X),
          prop_location_score2_features.PropLocationScore2Features(self.X),
          prop_log_historical_price_features.PropLogHistoricalPriceFeatures(self.X),
          price_usd_features.PriceUsdFeatures(self.X),
          srch_destination_id_features.SrchDestinationIdFeatures(self.X),
          srch_length_of_stay_features.SrchLengthOfStayFeatures(self.X),
          srch_booking_window_features.SrchBookingWindowFeatures(self.X),
          ]

      return map(self.transformer, feature_list)
  


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate features using train/test data")
    parser.add_argument("--test", action="store_true", default=False, help="Weather to use test data", required=False)
    result = parser.parse_args()

    if result.test:
        print("Reading test data")
        data = data_io.read_test()
    else:
        print("Reading training data")
        data = data_io.read_train()

    fm = FeatureExtractor(data)
    derived_features = fm.feature_extractor()
    data.fillna(0, inplace=True)
    data = pandas.concat([data] + derived_features, axis=1)
  
    if result.test:
        data_io.save_test_features(data)
    else:
        data_io.save_train_features(data)
      
