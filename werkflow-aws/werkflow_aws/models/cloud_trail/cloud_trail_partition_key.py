from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailPartitionKey(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
