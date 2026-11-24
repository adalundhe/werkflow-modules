from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEndpointServicePermissionsRequest(BaseModel):
    ServiceId: StrictStr
    DryRun: StrictBool | None = None
    AddAllowedPrincipals: list[StrictStr] | None = None
    RemoveAllowedPrincipals: list[StrictStr] | None = None
    PermissionType: Literal['vpc-endpoint', 'transit-gateway-attachment'] | None = None
