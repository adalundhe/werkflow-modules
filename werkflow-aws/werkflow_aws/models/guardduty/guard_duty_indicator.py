from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyIndicator(BaseModel):
    Key: StrictStr | None = None
    Values: list[StrictStr] | None = None
    Title: StrictStr | None = None
