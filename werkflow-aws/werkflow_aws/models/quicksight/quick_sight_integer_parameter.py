from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightIntegerParameter(BaseModel):
    Name: StrictStr | None = None
    Values: list[StrictInt] | None = None
