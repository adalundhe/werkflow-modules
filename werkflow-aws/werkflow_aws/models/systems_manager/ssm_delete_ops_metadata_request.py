from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteOpsMetadataRequest(BaseModel):
    OpsMetadataArn: StrictStr
