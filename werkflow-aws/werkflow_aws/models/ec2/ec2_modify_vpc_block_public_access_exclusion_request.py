from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcBlockPublicAccessExclusionRequest(BaseModel):
    ExclusionId: StrictStr
    InternetGatewayExclusionMode: Literal['allow-bidirectional', 'allow-egress']
    DryRun: StrictBool | None = None
