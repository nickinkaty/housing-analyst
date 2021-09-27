import {useEffect, useState} from "react";
import axios from "axios";

import Table from "../components/Table/Table";

const COLUMNS = ["Zipcode", "Total Real Estate", "AVG Price", "AVG Bathroom", "AVG Bedrooms", "AVG Price Change", "AVG Days On Zillow"]

const Analyst = () => {
  const [analystData, setAnalystData] = useState([]);

  const getRealEstateAnalyst = async () => {
    const res = await axios.get('http://172.18.0.4:5000/api/v1/realEstates/analyst');
    setAnalystData(res.data.data['realEstates']);
  };

  useEffect(()=> {
    getRealEstateAnalyst();
  },[])

  return (
      <>
        <Table COLUMNS={COLUMNS} data={analystData}/>
        <div>
          dsffdfsfdssdf
        </div>
      </>
  )
}

export default Analyst