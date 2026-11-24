from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTopicIRComparisonMethod(BaseModel):
    Type: StrictStr | None = None
    Period: StrictStr | None = None
    WindowSize: StrictInt | None = None
