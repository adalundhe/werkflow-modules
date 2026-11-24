from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3ScanRange(BaseModel):
    Start: StrictInt | None = None
    End: StrictInt | None = None
