import psycopg2
import yaml
import pandas as pd
from io import StringIO
from pathlib import Path
import os


def get_playoffs():
    playoffs_query = """
SELECT "Week", 
"Bracket", 
"Manager", 
"Team",
"Finish", 
"Playoff Seed", 
"Wk W/L", 
"Wk Pts", 
"Wk Pro. Pts", 
"Opp Manager", 
"Opp Wk Pts", 
"Opp Wk Pro. Pts" 
FROM prod.playoff_board
ORDER BY "Week", 
"Finish"
"""
    playoffs_df = DatabaseCursor().copy_from_psql(playoffs_query)
    return playoffs_df


def get_reg_season():
    weekly_rankings_query = """
SELECT "Week", 
"Manager", 
"Team",
"Cur. Wk Rk", 
"Prev. Wk Rk", 
"2pt Ttl", 
"2pt Ttl Rk", 
"Ttl Pts Win", 
"Win Ttl",
"Loss Ttl", 
"Ttl Pts", 
"Ttl Pts Rk" 
FROM prod.reg_season_results
ORDER BY "Week", 
"Cur. Wk Rk"
"""
    weekly_rankings_df = DatabaseCursor().copy_from_psql(weekly_rankings_query)
    return weekly_rankings_df


class DatabaseCursor(object):
    def __init__(self):
        """
        Import database credentials

        credential_file = path to private yaml file
        kwargs = {option_schema: "raw"}
        """
        credential_file = Path(
            "static/private.yaml"
        )

        with open(credential_file) as file:
            self.credentials = yaml.load(file, Loader=yaml.SafeLoader)

        self.db_url = self.credentials["heroku_db_url"]
        # self.db_url = os.environ["DATABASE_URL"]

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
