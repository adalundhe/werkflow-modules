from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .ec2_added_principal import EC2AddedPrincipal


class EC2ModifyVpcEndpointServicePermissionsResponse(BaseModel):
    AddedPrincipals: list[EC2AddedPrincipal] | None = None
    ReturnValue: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
