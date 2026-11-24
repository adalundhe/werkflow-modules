from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_network_interface_permission_state import EC2NetworkInterfacePermissionState


class EC2NetworkInterfacePermission(BaseModel):
    NetworkInterfacePermissionId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    AwsService: StrictStr | None = None
    Permission: StrictStr | None = None
    PermissionState: EC2NetworkInterfacePermissionState | None = None
