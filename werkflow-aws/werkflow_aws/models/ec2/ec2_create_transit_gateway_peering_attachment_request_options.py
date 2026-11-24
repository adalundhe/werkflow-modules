from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2CreateTransitGatewayPeeringAttachmentRequestOptions(BaseModel):
    DynamicRouting: Literal['enable', 'disable'] | None = None
    AllowMultipathResilience: StrictBool | None = None
    MultipathResilienceMode: Literal['always-on'] | None = None
