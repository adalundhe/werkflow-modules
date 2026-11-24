from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2ModifyVpcBlockPublicAccessOptionsRequest(BaseModel):
    InternetGatewayBlockMode: Literal['off', 'block-bidirectional', 'block-ingress']
    DryRun: StrictBool | None = None
