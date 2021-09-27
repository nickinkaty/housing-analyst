import format from "pg-format";
// import { jsonArrayToNestedArray } from "../helpers/convert_data_structures";
import pool from "../db/pool.js";
import { successMessage, errorMessage, status } from "../helpers/status";
import { hasDuplicates, isEmptyOrExist } from "../helpers/post_validation";
import { jsonArrayToNestedArray } from "../helpers/convert_data_structures";

const createZillowUrlParameters = async (req, res) => {
  const zillowUrlParameters = jsonArrayToNestedArray(req.body);

  console.log("zillow url parameters", zillowUrlParameters);

  // RESET zillowUrlParameters TABLE
  pool.query("DELETE FROM zillow_url_parameter;");

  if (
    isEmptyOrExist(zillowUrlParameters[0]) ||
    isEmptyOrExist(zillowUrlParameters)
  ) {
    errorMessage.error =
      "POST body is empty! Unable to create zillow url parameters!";
    return res.status(status.error).send(errorMessage);
  }

  if (hasDuplicates(zillowUrlParameters)) {
    errorMessage.error =
      "Duplicates Found! Unable to create zillow url parameters!";
    return res.status(status.error).send(errorMessage);
  }

  // CREATE SQL QUERY
  const createZillowUrlParametersQuery = format(
    `
    INSERT INTO
        zillow_url_parameter (
          region_id,
          region_type,
          zipcode,
          west,
          east,
          north,
          south
        )
    VALUES
    %L RETURNING *`,
    zillowUrlParameters
  );

  await pool
    .query(createZillowUrlParametersQuery)
    .then((queryRes) => {
      console.log(queryRes.rows);
      successMessage.message = "Successfully created zillow url parameters!";
      successMessage.count = queryRes.rowCount;
      successMessage.data = queryRes.rows;
      return res.status(status.created).send(successMessage);
    })
    .catch((queryErr) => {
      errorMessage.error = "Unable to create zillow url parameters!";
      return res.status(status.error).send(errorMessage);
    });
};

const getAllZillowUrlParameters = async (req, res) => {
  // CREATE SQL QUERY
  const getAllZillowUrlParametersQuery = `SELECT * FROM zillow_url_parameter;`;

  await pool
    .query(getAllZillowUrlParametersQuery)
    .then((queryRes) => {
      console.log(queryRes.rowCount, "3333");
      successMessage.count = queryRes.rowCount;
      successMessage.data = queryRes.rows;
      return res.status(status.created).send(successMessage);
    })
    .catch((queryErr) => {
      errorMessage.error = "Unable to fetch zillow url parameters!";
      return res.status(status.error).send(errorMessage);
    });
};

export { createZillowUrlParameters, getAllZillowUrlParameters };
