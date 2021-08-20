import format from "pg-format";
import { jsonArrayToNestedArray } from "../helpers/convert_data_structures";
import pool from "../db/pool.js";
import { successMessage, errorMessage, status } from "../helpers/status";

const createRealEstates = async (req, res) => {
  const createRealEstateArray = jsonArrayToNestedArray(req.body);

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

  console.log(sql);

  pool
    .query(sql)
    .then((queryRes) => {
      successMessage.count = queryRes.rowCount;
      successMessage.data = queryRes.rows[0];
      return res.status(status.created).send(successMessage);
    })
    .catch((queryErr) => {
      errorMessage.error = "Unable to create Real Estates";
      return res.status(status.error).send(errorMessage);
    });
};

const createRealEstatessss = async (req, res) => {
  console.log("test");
  console.log(req.body);
  console.log(res);
  // const {} = req.body;
  return res.status("200").send("successMessage");
};

export { createRealEstates, createRealEstatessss };
