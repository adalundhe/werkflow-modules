from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyModelDetail(BaseModel):
    ModelId: StrictStr | None = None
