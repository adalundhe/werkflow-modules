from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .macie_range import MacieRange


class MaciePage(BaseModel):
    lineRange: MacieRange | None = None
    offsetRange: MacieRange | None = None
    pageNumber: StrictInt | None = None
