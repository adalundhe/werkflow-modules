from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDataLakeReplicationConfiguration(BaseModel):
    regions: list[StrictStr] | None = None
    roleArn: StrictStr | None = None
