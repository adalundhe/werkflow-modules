from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightApplicableTo(BaseModel):
    Type: StrictStr | None = None
    GroupArns: list[StrictStr] | None = None
