from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_volume_permission_modifications import EC2CreateVolumePermissionModifications


class EC2ModifySnapshotAttributeRequest(BaseModel):
    SnapshotId: StrictStr
    Attribute: Literal['productCodes', 'createVolumePermission'] | None = None
    CreateVolumePermission: EC2CreateVolumePermissionModifications | None = None
    GroupNames: list[StrictStr] | None = None
    OperationType: Literal['add', 'remove'] | None = None
    UserIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
