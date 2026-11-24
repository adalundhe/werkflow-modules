from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AthenaQueryRuntimeStatisticsRows(BaseModel):
    InputRows: StrictInt | None = None
    InputBytes: StrictInt | None = None
    OutputBytes: StrictInt | None = None
    OutputRows: StrictInt | None = None
