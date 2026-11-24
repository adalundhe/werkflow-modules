from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetVerifiedAccessEndpointTargetsRequest(BaseModel):
    VerifiedAccessEndpointId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
