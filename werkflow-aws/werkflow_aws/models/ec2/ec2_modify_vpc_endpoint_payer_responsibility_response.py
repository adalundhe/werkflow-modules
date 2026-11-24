from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_payer_responsibility_entry import EC2PayerResponsibilityEntry


class EC2ModifyVpcEndpointPayerResponsibilityResponse(BaseModel):
    VpcEndpointId: StrictStr | None = None
    PayerResponsibilities: list[EC2PayerResponsibilityEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
