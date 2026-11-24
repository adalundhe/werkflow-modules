from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LightsailWafResponseInspection(BaseModel):
    successCodes: list[StrictInt] | None = None
    failureCodes: list[StrictInt] | None = None
