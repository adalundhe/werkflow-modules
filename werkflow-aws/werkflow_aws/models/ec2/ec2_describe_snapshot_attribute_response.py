from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_create_volume_permission import EC2CreateVolumePermission
from .ec2_product_code import EC2ProductCode


class EC2DescribeSnapshotAttributeResponse(BaseModel):
    ProductCodes: list[EC2ProductCode] | None = None
    SnapshotId: StrictStr | None = None
    CreateVolumePermissions: list[EC2CreateVolumePermission] | None = None
    ResponseMetadata: dict[str, Any] | None = None
