from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneEnvironmentResolvedAccount(BaseModel):
    awsAccountId: StrictStr | None = None
    regionName: StrictStr | None = None
    sourceAccountPoolId: StrictStr | None = None
