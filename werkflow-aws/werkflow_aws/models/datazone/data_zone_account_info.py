from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAccountInfo(BaseModel):
    awsAccountId: StrictStr | None = None
    supportedRegions: list[StrictStr] | None = None
    awsAccountName: StrictStr | None = None
