from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectThreshold(BaseModel):
    Comparison: StrictStr | None = None
    ThresholdValue: StrictFloat | StrictInt | None = None
