from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ECSTotalLocalStorageGBRequest(BaseModel):
    min: StrictFloat | StrictInt | None = None
    max: StrictFloat | StrictInt | None = None
