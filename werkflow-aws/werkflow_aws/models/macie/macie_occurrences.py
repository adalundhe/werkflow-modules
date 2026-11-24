from __future__ import annotations
from pydantic import BaseModel
from .macie_cell import MacieCell
from .macie_page import MaciePage
from .macie_range import MacieRange
from .macie_record import MacieRecord


class MacieOccurrences(BaseModel):
    cells: list[MacieCell] | None = None
    lineRanges: list[MacieRange] | None = None
    offsetRanges: list[MacieRange] | None = None
    pages: list[MaciePage] | None = None
    records: list[MacieRecord] | None = None
