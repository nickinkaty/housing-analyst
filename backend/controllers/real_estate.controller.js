import format from "pg-format";
import { jsonArrayToNestedArray } from "../helpers/convert_data_structures";
import pool from "../db/pool.js";
import { successMessage, errorMessage, status } from "../helpers/status";

const createRealEstates = async (req, res) => {
  const createRealEstateArray = jsonArrayToNestedArray(req.body);
  // pool.query("DELETE FROM real_estate;");

  // CREATE SQL QUERY
  const sql = format(
    `
    INSERT INTO
        real_estate (
          zpid,
          bathrooms,
          bedrooms,
          city,
          country,
          currency,
          date_price_changed,
          date_sold,
          days_on_zillow,
          detail_url,
          grouping_name,
          home_status,
          home_status_for_hdp,
          home_type,
          img_src,
          living_area,
          lot_area_unit,
          lot_area_value,
          price,
          price_change,
          price_reduction,
          rent_zestimate,
          state,
          street_address,
          tax_assessed_value,
          time_on_zillow,
          zestimate,
          zipcode
        )
    VALUES
    %L`,
    createRealEstateArray
  );

  await pool
    .query(sql)
    .then((queryRes) => {
      successMessage.count = queryRes.rowCount;
      successMessage.data = queryRes.rows[0];
      return res.status(status.created).send(successMessage);
    })
    .catch((queryErr) => {
      console.log(queryErr);
      errorMessage.error = "Unable to create Real Estates";
      return res.status(status.error).send(errorMessage);
    });
};

const getRealEstate = async (req, res) => {
  console.log(req);
  let realEstates = [];
  res.status(status.success).json({
    status: "success",
    result: realEstates.length,
    data: {
      realEstates,
    },
  });
};

const getRealEstateAnalyst = async (req, res) => {
  let realEstates = [];
  const sql = `
    SELECT 
        zipcode, 
        COUNT(*) as "totalRealEstate", 
        AVG(price) as "avgPrice", 
        AVG(bathrooms) as "avgBathrooms",
        AVG(bedrooms) as "avgBedrooms",
        AVG(price) as "avgPrice",
        AVG(price_change) as "avgPriceChange",
        AVG(days_on_zillow) as "avgDaysOnZillow"
    FROM 
        real_estate 
    GROUP BY 
        zipcode;`;

  await pool
    .query(sql)
    .then((queryRes) => {
      realEstates = queryRes.rows;
      // console.log(queryRes);
      res.status(status.success).json({
        status: "success",
        result: realEstates.length,
        data: {
          realEstates,
        },
      });
    })
    .catch((queryErr) => {
      console.log(queryErr);
      errorMessage.error = "Unable to create Real Estates";
      return res.status(status.error).send(errorMessage);
    });
};

export { createRealEstates, getRealEstate, getRealEstateAnalyst };
