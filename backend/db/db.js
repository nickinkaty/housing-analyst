import pool from "./pool";

pool.on("connect", () => {
  console.log("connected to the Database");
});

export default pool;
