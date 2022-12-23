import psycopg2
import yaml
import pandas as pd
from io import StringIO
from pathlib import Path
import os


def prod_reg_season_results_tbl():
    return DatabaseCursor().copy_from_psql("""SELECT * FROM prod.reg_season_results""")


def prod_playoff_board_tbl():
    return DatabaseCursor().copy_from_psql("""SELECT * FROM prod.playoff_board""")


class DatabaseCursor(object):
    def __init__(self):
        """
        Import database credentials

        credential_file = path to private yaml file
        kwargs = {option_schema: "raw"}
        """

        try:
            self.db_url = os.environ["DATABASE_URL"]

        except:
            credential_file = Path("static/private.yaml")
            with open(credential_file) as file:
                self.credentials = yaml.load(file, Loader=yaml.SafeLoader)

            self.db_url = self.credentials["heroku_db_url"]

    def __enter__(self):
        """
        Set up connection and cursor
        """
        self.conn = psycopg2.connect(
            self.db_url,
            sslmode="require",
        )
        self.cur = self.conn.cursor()

        return self.cur

    def __exit__(self, exc_result):
        """
        Close connection and cursor

        exc_results = bool
        """

        if exc_result == True:
            self.conn.commit()

        self.cur.close()
        self.conn.close()

    def copy_to_psql(self, df, table):
        """
        Copy table to postgres from a pandas dataframe
        in memory using StringIO
        https://naysan.ca/2020/05/09/pandas-to-postgresql-using-psycopg2-bulk-insert-performance-benchmark/
        https://stackoverflow.com/questions/23103962/how-to-write-dataframe-to-postgres-table

        table = "test"
        df = pd.DataFrame()
        first_time = "NO"
        """

        buffer = StringIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)

        cursor = self.__enter__()
        copy_to = f"BEGIN; \
                        DELETE FROM {table}; \
                        COPY {table} FROM STDIN WITH (FORMAT CSV, HEADER TRUE); \
                    END;"
        cursor.copy_expert(copy_to, buffer)
        self.__exit__(exc_result=True)

    def copy_from_psql(self, query):
        """
        Copy data from Postgresql Query into
        Pandas dataframe
        https://towardsdatascience.com/optimizing-pandas-read-sql-for-postgres-f31cd7f707ab

        query = "select * from raw.test"
        """
        cursor = self.__enter__()

        sql_query = f"COPY ({query}) TO STDOUT WITH (FORMAT CSV, HEADER TRUE);"
        buffer = StringIO()

        cursor.copy_expert(sql_query, buffer)
        buffer.seek(0)
        df = pd.read_csv(buffer)
        self.__exit__(exc_result=True)

        return df
