from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEndpointServicePayerResponsibilityRequest(BaseModel):
    ServiceId: StrictStr
    PayerResponsibility: Literal['ServiceOwner']
    DryRun: StrictBool | None = None
