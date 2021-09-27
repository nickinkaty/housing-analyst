import styles from './Header.module.css'

const Header = (props) => {
  const {COLUMNS} = props;

  return (
      <div className={styles['table-row']}>
        {COLUMNS.map((column) => (
            <div key={column} className={styles['table-cell']}>
              {column}
            </div>
          ))}
      </div>
  )
}

export default Header;