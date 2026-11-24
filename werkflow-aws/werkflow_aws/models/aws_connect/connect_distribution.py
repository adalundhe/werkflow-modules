from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectDistribution(BaseModel):
    Region: StrictStr | None = None
    Percentage: StrictInt | None = None
