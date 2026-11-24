from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2RegionalSummary(BaseModel):
    RegionName: StrictStr | None = None
    NumberOfMatchedAccounts: StrictInt | None = None
    NumberOfUnmatchedAccounts: StrictInt | None = None
