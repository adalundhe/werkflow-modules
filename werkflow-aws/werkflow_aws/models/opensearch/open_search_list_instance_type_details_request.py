from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class OpenSearchListInstanceTypeDetailsRequest(BaseModel):
    EngineVersion: StrictStr
    DomainName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    RetrieveAZs: StrictBool | None = None
    InstanceType: StrictStr | None = None
