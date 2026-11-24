from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class TimestreamQueryQueryStatus(BaseModel):
    ProgressPercentage: StrictFloat | StrictInt | None = None
    CumulativeBytesScanned: StrictInt | None = None
    CumulativeBytesMetered: StrictInt | None = None
