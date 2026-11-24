from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_allowed_principal import EC2AllowedPrincipal


class EC2DescribeVpcEndpointServicePermissionsResponse(BaseModel):
    AllowedPrincipals: list[EC2AllowedPrincipal] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
