import Header from "./Header/Header";
import Rows from "./Rows/Rows";
import styles from "./Table.module.css"


const Table = (props) => {
  const {COLUMNS, data} = props;

  return (
      <div className={styles.table}>
        <Header COLUMNS={COLUMNS} />
        <Rows data={data} />
      </div>
  )
}

export default Table;