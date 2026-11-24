from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDeleteVpcConnectorRequest(BaseModel):
    VpcConnectorArn: StrictStr
