from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectThresholdV2(BaseModel):
    Comparison: StrictStr | None = None
    ThresholdValue: StrictFloat | StrictInt | None = None
