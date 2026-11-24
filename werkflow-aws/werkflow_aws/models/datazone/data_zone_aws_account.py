from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAwsAccount(BaseModel):
    awsAccountId: StrictStr | None = None
    awsAccountIdPath: StrictStr | None = None
