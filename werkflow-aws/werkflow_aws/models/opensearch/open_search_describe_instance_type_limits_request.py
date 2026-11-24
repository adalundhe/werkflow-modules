from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeInstanceTypeLimitsRequest(BaseModel):
    InstanceType: StrictStr
    EngineVersion: StrictStr
    DomainName: StrictStr | None = None
