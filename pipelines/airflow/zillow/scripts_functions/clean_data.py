import ast
import json
import time

from pyspark.sql import SparkSession
from pyspark.shell import sc


def clean_real_estate_data(real_estate_results) -> str:
    # print(real_estate_results[0])

    # GET HOME INFO AND CREATE 2 NEW KEYS IMG SRC AND IMG DETAIL
    real_estates_info = []
    for real_estate_result in real_estate_results:
        real_estate_result['hdpData']['homeInfo']['imgSrc'] = real_estate_result['imgSrc']
        real_estate_result['hdpData']['homeInfo']['detailUrl'] = real_estate_result['detailUrl']

        real_estate_result['hdpData']['homeInfo']['grouping_name'] = ''
        if "grouping_name" in real_estate_result:
            real_estate_result['hdpData']['homeInfo']['grouping_name'] = real_estate_result['grouping_name']

        real_estates_info.append(real_estate_result['hdpData']['homeInfo'])

    # CONVERT PY-LITERAL -> CLEAN JSON
    real_estates_info = json.dumps(real_estates_info)

    # INITIALIZE SPARK
    spark = SparkSession.builder.appName('Dataframe').getOrCreate()

    real_estates_info_rdd = sc.parallelize([real_estates_info])

    # FILL NULL TO STRING NULL
    df = spark.read.json(real_estates_info_rdd)

    # DROP UNUSED COLUMNS
    df = df.drop(
        *['group_type', 'brokerId', 'isFeatured', 'isNonOwnerOccupied', 'isPreforeclosureAuction', 'isPremierBuilder',
          'isUnmappable', 'isZillowOwned', 'latitude', 'listing_sub_type', 'longitude', 'newConstructionType',
          'openHouse', 'open_house_info', 'priceForHDP', 'priceSuffix', 'providerListingID', 'shouldHighlight', 'unit',
          'tvCollectionImageLink', 'tvHighResImageLink', 'desktopWebHdpImageLink', 'hiResImageLink', 'imageLink',
          'mediumImageLink', 'tvImageLink', 'watchImageLink', 'videoCount'])

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

    final_df = reorder_columns_df.orderBy('zpid').dropDuplicates(subset=['zpid'])

    # CONVERT PYSPARK DATAFRAME TO JSON STR ARRAY
    str_json_array = final_df.na.fill("null").na.fill(0).toJSON().collect()

    # ARRAY OF JSON STR TO JSON OBJECT EX: ['{}'] =>[{}]
    output_list = ast.literal_eval(json.dumps([json.loads(json_string) for json_string in str_json_array]))

    return output_list
