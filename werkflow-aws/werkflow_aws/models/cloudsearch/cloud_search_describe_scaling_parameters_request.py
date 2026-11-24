from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDescribeScalingParametersRequest(BaseModel):
    DomainName: StrictStr
