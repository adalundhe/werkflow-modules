from __future__ import annotations
from pydantic import BaseModel
from .ec2_create_volume_permission import EC2CreateVolumePermission


class EC2CreateVolumePermissionModifications(BaseModel):
    Add: list[EC2CreateVolumePermission] | None = None
    Remove: list[EC2CreateVolumePermission] | None = None
