import format from "pg-format";
// import { jsonArrayToNestedArray } from "../helpers/convert_data_structures";
import pool from "../db/pool.js";
import { successMessage, errorMessage, status } from "../helpers/status";

const createZillowUrlParameters = async (req, res) => {
  const zillowUrlParameters = req.body;

  console.log(zillowUrlParameters);

  return res.status(200).send("TEST !!!!!");
  // LOOP
  // Object.keys(zillowUrlParameters).forEach((zipcode) => {
  //   console.log(
  //     "Key : " + zipcode + ", Value : " + zillowUrlParameters[zipcode]
  //   );
  // });

  // CREATE SQL QUERY
  // const sql = format(
  //   `
  //   INSERT INTO
  //       real_estate (
  //         region_id
  //       )
  //   VALUES
  //   %L`,
  //   createRealEstateArray
  // );

  // pool
  //   .query(sql)
  //   .then((queryRes) => {
  //     successMessage.count = queryRes.rowCount;
  //     successMessage.data = queryRes.rows[0];
  //     return res.status(status.created).send(successMessage);
  //   })
  //   .catch((queryErr) => {
  //     errorMessage.error = "Unable to create Region Ids";
  //     return res.status(status.error).send(errorMessage);
  //   });
};

export { createZillowUrlParameters };
