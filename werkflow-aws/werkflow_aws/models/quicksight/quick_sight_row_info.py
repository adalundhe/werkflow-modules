from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QuickSightRowInfo(BaseModel):
    RowsIngested: StrictInt | None = None
    RowsDropped: StrictInt | None = None
    TotalRowsInDataset: StrictInt | None = None
