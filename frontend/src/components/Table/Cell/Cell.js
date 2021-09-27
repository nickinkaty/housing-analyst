import styles from './Cell.module.css'


const Cell = (props) => {
  const {dataObj} = props;
  return (
      <>
        {Object.keys(dataObj).map(key => (
            <div className={styles["table-cell"]}>
              {dataObj[key]}
            </div>
        ))}
      </>
  )
}

export default Cell;