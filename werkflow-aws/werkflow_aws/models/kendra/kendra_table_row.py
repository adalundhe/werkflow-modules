from __future__ import annotations
from pydantic import BaseModel
from .kendra_table_cell import KendraTableCell


class KendraTableRow(BaseModel):
    Cells: list[KendraTableCell] | None = None
