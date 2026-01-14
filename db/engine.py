# db/engine.py

from db.database import Database
from db.table import Table, Column


class Engine:
    def __init__(self, database: Database):
        self.database = database

    def execute(self, command: str):
        command = command.strip()

        if command.upper().startswith("CREATE TABLE"):
            return self._create_table(command)

        raise ValueError(f"Unsupported command: {command}")

    def _create_table(self, command: str):
        """
        Example:
        CREATE TABLE users (id INT PRIMARY KEY, name TEXT)
        """
        try:
            before_paren, inside_paren = command.split("(", 1)
            inside_paren = inside_paren.rstrip(")")

            _, _, table_name = before_paren.strip().split()

            columns = []
            for col_def in inside_paren.split(","):
                parts = col_def.strip().split()

                name = parts[0]
                dtype = parts[1]

                primary_key = "PRIMARY" in parts
                unique = "UNIQUE" in parts

                columns.append(
                    Column(
                        name=name,
                        dtype=dtype,
                        primary_key=primary_key,
                        unique=unique,
                    )
                )

            table = Table(table_name, columns)
            self.database.create_table(table)

            return f"Table '{table_name}' created"

        except Exception as e:
            raise ValueError(f"Invalid CREATE TABLE syntax: {e}")
