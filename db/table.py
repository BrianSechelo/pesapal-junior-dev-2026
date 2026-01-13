# db/table.py

from typing import Any, Dict, List


class Column:
    def __init__(
        self,
        name: str,
        dtype: str,
        primary_key: bool = False,
        unique: bool = False,
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

        # Column lookup
        self.column_map = {col.name: col for col in columns}

        # Primary key (only one allowed)
        self.primary_key = next(
            (col.name for col in columns if col.primary_key), None
        )

        # Unique + primary key indexes
        self.unique_indexes = {
            col.name: set()
            for col in columns
            if col.unique or col.primary_key
        }

    def insert(self, row: Dict[str, Any]):
        # Ensure all columns exist
        for col in self.columns:
            if col.name not in row:
                raise ValueError(f"Missing value for column '{col.name}'")

        # Enforce unique constraints
        for col_name, index in self.unique_indexes.items():
            value = row[col_name]
            if value in index:
                raise ValueError(
                    f"Duplicate value '{value}' for unique column '{col_name}'"
                )

        # Insert row
        self.rows.append(row)

        # Update indexes
        for col_name, index in self.unique_indexes.items():
            index.add(row[col_name])

    def select_all(self):
        return self.rows
