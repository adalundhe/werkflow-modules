from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_network_interface_permission import EC2NetworkInterfacePermission


class EC2CreateNetworkInterfacePermissionResponse(BaseModel):
    InterfacePermission: EC2NetworkInterfacePermission | None = None
    ResponseMetadata: dict[str, Any] | None = None
