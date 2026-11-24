from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class ConfigServiceComplianceContributorCount(BaseModel):
    CappedCount: StrictInt | None = None
    CapExceeded: StrictBool | None = None
