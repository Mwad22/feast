from feast import FeatureStore
import pandas as pd
from datetime import datetime

entity_df = pd.DataFrame.from_dict({
    "driver_id": [1001, 1002, 1003, 1004],
    "event_timestamp": [
        datetime(2021, 4, 12, 10, 59, 42),
        datetime(2021, 4, 12, 8,  12, 10),
        datetime(2021, 4, 12, 16, 40, 26),
        datetime(2021, 4, 12, 15, 1 , 12)
    ]
})

store = FeatureStore(repo_path=".")


print("***************TEST************")
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:conv_rate',
        'driver_hourly_stats:avg_daily_trips',
        'driver_monthly_stats:avg_daily_trips',
        'driver_monthly_stats:acc_rate', 
        'driver_monthly_stats:conv_rate',

    ], 
).to_df()

print(training_df)

for feature_name in training_df.columns:
    print(feature_name)


print("***************TEST 2************")
training_df = store.get_historical_features(
    entity_df=entity_df, 
    feature_refs = [
        'driver_hourly_stats:conv_rate',
        #'driver_hourly_stats:avg_daily_trips',
        'driver_monthly_stats:avg_daily_trips',
        'driver_monthly_stats:acc_rate', 
        #'driver_monthly_stats:conv_rate',

    ], 
    feature_names_only = True,
).to_df()

print(training_df)

for feature_name in training_df.columns:
    print(feature_name)