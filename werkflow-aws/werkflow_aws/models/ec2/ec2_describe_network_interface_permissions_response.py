from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_interface_permission import EC2NetworkInterfacePermission


class EC2DescribeNetworkInterfacePermissionsResponse(BaseModel):
    NetworkInterfacePermissions: list[EC2NetworkInterfacePermission] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
