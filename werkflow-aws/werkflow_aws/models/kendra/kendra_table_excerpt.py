from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .kendra_table_row import KendraTableRow


class KendraTableExcerpt(BaseModel):
    Rows: list[KendraTableRow] | None = None
    TotalNumberOfRows: StrictInt | None = None
