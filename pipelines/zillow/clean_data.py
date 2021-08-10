import ast
import json

from pyspark.shell import sc
from pyspark.sql import SparkSession


def clean_real_estates_data(real_estate_results):
    # GET HOME INFO AND CREATE 2 NEW KEYS IMG SRC AND IMG DETAIL
    real_estates_info = []
    for real_estate_result in real_estate_results:
        real_estate_result['hdpData']['homeInfo']['imgSrc'] = real_estate_result['imgSrc']
        real_estate_result['hdpData']['homeInfo']['detailUrl'] = real_estate_result['detailUrl']
        real_estates_info.append(real_estate_result['hdpData']['homeInfo'])

    # CONVERT PY-LITERAL -> CLEAN JSON
    real_estates_info = json.dumps(real_estates_info)

    # INITIALIZE SPARK
    spark = SparkSession.builder.appName('Dataframe').getOrCreate()

    # FILL NULL TO STRING NULL
    df = spark.read.json(sc.parallelize([real_estates_info]))

    df = df.na.fill('test')

    # DROP UNUSED COLUMNS
    df = df.drop(
        *['group_type', 'brokerId', 'isFeatured', 'isNonOwnerOccupied', 'isPreforeclosureAuction', 'isPremierBuilder',
          'isUnmappable', 'isZillowOwned', 'latitude', 'listing_sub_type', 'longitude', 'newConstructionType',
          'openHouse', 'open_house_info', 'priceForHDP', 'priceSuffix', 'providerListingID', 'shouldHighlight', 'unit',
          'tvCollectionImageLink', 'tvHighResImageLink', 'desktopWebHdpImageLink', 'hiResImageLink', 'imageLink',
          'mediumImageLink', 'tvImageLink', 'watchImageLink'])

    # RENAME AND REORDER COLUMNS NAMES
    df_columns_dict = {
        "zpid": "zpid",
        "bathrooms": "bathrooms",
        "bedrooms": "bedrooms",
        "city": "city",
        "country": "country",
        "currency": "currency",
        "datePriceChanged": "date_price_changed",
        "dateSold": "date_sold",
        "daysOnZillow": "days_on_zillow",
        "detailUrl": "detail_url",
        "grouping_name": "grouping_name",
        "homeStatus": "home_status",
        "homeStatusForHDP": "home_status_for_hdp",
        "homeType": "home_type",
        "imgSrc": "img_src",
        "livingArea": "living_area",
        "lotAreaUnit": "lot_area_unit",
        "lotAreaValue": "lot_area_value",
        "price": "price",
        "priceChange": "price_change",
        "priceReduction": "price_reduction",
        "rentZestimate": "rent_zestimate",
        "state": "state",
        "streetAddress": "street_address",
        "taxAssessedValue": "tax_assessed_value",
        "timeOnZillow": "time_on_zillow",
        "zestimate": "zestimate",
        "zipcode": "zipcode"
    }

    # RENAME COLUMNS
    rename_columns_df = df.toDF(*[df_columns_dict[col] for col in df.columns])

    # REORDER COLUMNS TO DICT
    columns_array = [df_columns_dict[col] for col in df_columns_dict]
    reorder_columns_df = rename_columns_df.select(*columns_array)

    # CONVERT PYSPARK DATAFRAME TO JSON STR ARRAY
    str_json_array = reorder_columns_df.na.fill("null").na.fill(0).toJSON().collect()

    # ARRAY OF JSON STR TO JSON OBJECT EX: ['{}'] =>[{}]
    output_list = ast.literal_eval(json.dumps([json.loads(json_string) for json_string in str_json_array]))

    return output_list
