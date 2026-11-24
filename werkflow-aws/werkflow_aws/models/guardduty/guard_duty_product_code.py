from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyProductCode(BaseModel):
    Code: StrictStr | None = None
    ProductType: StrictStr | None = None
