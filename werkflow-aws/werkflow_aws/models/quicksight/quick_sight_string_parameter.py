from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStringParameter(BaseModel):
    Name: StrictStr | None = None
    Values: list[StrictStr] | None = None
