from __future__ import annotations
from pydantic import BaseModel
from .ec2_launch_permission import EC2LaunchPermission


class EC2LaunchPermissionModifications(BaseModel):
    Add: list[EC2LaunchPermission] | None = None
    Remove: list[EC2LaunchPermission] | None = None
