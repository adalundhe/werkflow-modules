from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2ResponseInspectionBodyContains(BaseModel):
    SuccessStrings: list[StrictStr] | None = None
    FailureStrings: list[StrictStr] | None = None
