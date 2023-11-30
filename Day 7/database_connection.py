import mysql.connector
import logging


DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'qu1Xkz'
DB_NAME = 'smite'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
error = mysql.connector.Error


def main():
    """Main function to execute the program."""
    # Establish the database connection
    conn = setup_connection()

    # Execute SELECT query and print results
    select_and_print_query(conn)

    # Close the connection
    close_conn(conn)


def setup_connection():
    """Set up a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            logger.info("Connection Established.")
        return connection
    except error as e:
        logger.error(f"Error during database connection: {e}")
        raise


def select_and_print_query(conn):
    """Execute a SELECT query, print the results and close the cursor."""
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM gods")
        rows = cursor.fetchall()
        header = [description[0] for description in cursor.description]

        print(header)
        for row in rows:
            print(row)
    except error as e:
        logger.error(f"Error during query execution: {e}")
        raise
    finally:
        cursor.close()


def close_conn(conn):
    """Close the database connection."""
    try:
        if conn.is_connected():
            conn.close()
            logger.info("Connection Closed.")
    except error as e:
        logger.error(f"Error during closing connection: {e}")


if __name__ == "__main__":
    main()
