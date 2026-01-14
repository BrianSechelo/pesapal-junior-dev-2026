# db/engine.py

from db.database import Database
from db.table import Table, Column


class Engine:
    def __init__(self, database: Database):
        self.database = database

    def execute(self, command: str):
        command = command.strip()

        upper = command.upper()

        if upper.startswith("CREATE TABLE"):
            return self._create_table(command)

        if upper.startswith("INSERT INTO"):
            return self._insert_into(command)

        if upper.startswith("SELECT"):
            return self._select(command)

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

    def _insert_into(self, command: str):
        """
        Example:
        INSERT INTO users VALUES (1, 'a@b.com', 'Alice')
        """
        try:
            before_paren, inside_paren = command.split("(", 1)
            inside_paren = inside_paren.rstrip(")")

            parts = before_paren.strip().split()

            table_name = parts[2]

            table = self.database.get_table(table_name)

            raw_values = [v.strip() for v in inside_paren.split(",")]

            values = []
            for v in raw_values:
                 # Remove quotes for TEXT
                if v.startswith("'") and v.endswith("'"):
                    values.append(v[1:-1])
                else:
                    values.append(int(v))
            if len(values) != len(table.columns):
                raise ValueError("Common count does not match value count")

            row = {
                table.columns[i].name: values[i]
                for i in range(len(values))
            }

            table.insert(row)

            return f"1 row inserted into '{table_name}'"

        except Exception as e:
            raise ValueError(f"Invalid INSERT syntax: {e}")

    def _select(self, command: str):
        """
        Example:
        SELECT * FROM users
        """
        try:
            parts = command.strip().split()

            if parts[1] != "*":
                raise ValueError("Only Select * is supported")

            table_name = parts[3]
            table = self.database.get_table(table_name)

            return table.select_all()

        except Exception as e:
            raise ValueError(f"Invalid SELECT syntax: {e}")