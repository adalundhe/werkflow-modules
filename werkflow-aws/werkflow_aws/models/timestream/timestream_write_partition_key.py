from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWritePartitionKey(BaseModel):
    Type: StrictStr | None = None
    Name: StrictStr | None = None
    EnforcementInRecord: StrictStr | None = None
