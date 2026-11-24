from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WAFv2ResponseInspectionStatusCode(BaseModel):
    SuccessCodes: list[StrictInt] | None = None
    FailureCodes: list[StrictInt] | None = None
