from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2ModifyTransitGatewayPeeringAttachmentRequestOptions(BaseModel):
    AllowMultipathResilience: StrictBool | None = None
    MultipathResilienceMode: Literal['always-on'] | None = None
