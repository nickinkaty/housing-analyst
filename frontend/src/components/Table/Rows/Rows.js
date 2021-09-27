import Cell from "../Cell/Cell";
import styles from "./Rows.module.css"

const Rows = (props) => {
  const {data} = props;

  return (
      <>
        {data.map((dataObj) => (
          <div className={styles["table-row"]}>
            <Cell dataObj={dataObj} />
            {/*Object.keys(obj).map(key => (*/}

            {/*    console.log(obj[key])*/}
            {/*));*/}
          </div>
        ))}
      </>
  )
}

export default Rows;