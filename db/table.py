from typing import Any, Dict, List

class Column:
    def __init__(
        self,
        name: str,
        dtype: str,
        primary_key: bool = False,
        unique = False,
    ):

        self.name = name
        self.dtype = dtype.upper()
        self.primary_key = primary_key
        self.unique = unique

class Table:
    def __init__(self, name: str, columns: List[Column]):
        self.name = name
        self.columns = columns
        self.rows: List[Dict[str, Any]] = []

        self.column_map = {col.name: col for col in columns}

        self.primary_key = next(
            (col.name for col in columns if col.primary_key), None
        )

        self.unique_indexes = {
            col.name: set() for col in columns if col.unique or col.primary_key
        }

    def insert(self, row: Dict[str, Any]):
        for col in self.columns:
            if col.name not in rows:
                raise ValueError(f"Missing value for column '{col.name}'")

        for col_name, index in self.unique_indexes.items():
            value = row[col_name]
            if value in index:
                raise ValueError(
                    f"Duplicate value '{value}' for unique column '{col_name}'"
                )
                # Insert
        self.rows.append(row)
         #Update indexes
         
        for col_name, index in self.unique_indexes.items():
            index.add(row[col_name])

    def select_all(self):
        return self.rows