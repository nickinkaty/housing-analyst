require = require("esm")(module /*, options*/);
import pool from "./pool";
import createRealEstateQuery from "../models/real_estate.model";

pool.on("connect", () => {
  console.log("connected to the Database");
});

// CREATE TABLE QUERY
const createTable = (creatTableQuery) => {
  pool
    .query(creatTableQuery)
    .then((res) => {
      console.log(res);
      pool.end();
    })
    .catch((err) => {
      console.log(err);
      pool.end();
    });
};

export const createAllTables = () => {
  const createTablesQueryArr = [createRealEstateQuery];
  createTablesQueryArr.forEach((createTablesQuery) => {
    createTable(createTablesQuery);
  });
};

createAllTables();

require("make-runnable");
