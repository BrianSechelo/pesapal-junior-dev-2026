# db/database.py

from typing import Dict
from db.table import Table


class Database:
    def __init__(self, name: str):
        self.name = name
        self.tables: Dict[str, Table] = {}

    def create_table(self, table: Table):
        if table.name in self.tables:
            raise ValueError(f"Table '{table.name}' already exists")

        self.tables[table.name] = table

    def get_table(self, table_name: str) -> Table:
        if table_name not in self.tables:
            raise ValueError(f"Table '{table_name}' does not exist")

        return self.tables[table_name]

    def list_tables(self):
        return list(self.tables.keys())
