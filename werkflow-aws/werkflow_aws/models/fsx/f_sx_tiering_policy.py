from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxTieringPolicy(BaseModel):
    CoolingPeriod: StrictInt | None = None
    Name: StrictStr | None = None
