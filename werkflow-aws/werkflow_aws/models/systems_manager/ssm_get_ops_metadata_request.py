from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMGetOpsMetadataRequest(BaseModel):
    OpsMetadataArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
