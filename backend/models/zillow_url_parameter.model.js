const createZillowUrlParameter = `
  CREATE TABLE IF NOT EXISTS zillow_url_parameter
    (
       region_id INT PRIMARY KEY,
       zipcode INT
    )`;

export default createZillowUrlParameter;
