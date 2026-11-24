from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AWSS3Progress(BaseModel):
    BytesScanned: StrictInt | None = None
    BytesProcessed: StrictInt | None = None
    BytesReturned: StrictInt | None = None
