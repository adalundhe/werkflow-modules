from __future__ import annotations
from pydantic import BaseModel
from .ec2_load_permission_request import EC2LoadPermissionRequest


class EC2LoadPermissionModifications(BaseModel):
    Add: list[EC2LoadPermissionRequest] | None = None
    Remove: list[EC2LoadPermissionRequest] | None = None
