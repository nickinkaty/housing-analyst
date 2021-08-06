const createRealEstateQuery = `
  CREATE TABLE IF NOT EXISTS real_estate
    (
       zpid                BIGINT PRIMARY KEY,
       bathrooms           SMALLINT,
       bedrooms            SMALLINT,
       city                VARCHAR(35),
       country             VARCHAR(35),
       currency            VARCHAR(6),
       date_price_changed  BIGINT,
       date_sold           BIGINT,
       days_on_zillow      INT,
       detail_url          VARCHAR(140),
       grouping_name       VARCHAR(35),
       home_status         VARCHAR(25),
       home_status_for_hdp VARCHAR(25),
       home_type           VARCHAR(25),
       img_src             VARCHAR(140),
       living_area         INT,
       lot_area_unit       INT,
       lot_area_value      INT,
       price               INT,
       price_change        INT,
       price_reduction     INT,
       rent_zestimate      INT,
       state               VARCHAR(25),
       street_address      VARCHAR(60),
       tax_assessed_value  INT,
       time_on_zillow      INT,
       zestimate           INT,
       zipcode             SMALLINT
    )`;

export default createRealEstateQuery;
