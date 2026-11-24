from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightGradientStop(BaseModel):
    GradientOffset: StrictFloat | StrictInt | None = None
    DataValue: StrictFloat | StrictInt | None = None
    Color: StrictStr | None = None
