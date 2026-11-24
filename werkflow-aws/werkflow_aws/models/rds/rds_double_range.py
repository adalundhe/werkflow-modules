from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RDSDoubleRange(BaseModel):
    From: StrictFloat | StrictInt | None = None
    To: StrictFloat | StrictInt | None = None
