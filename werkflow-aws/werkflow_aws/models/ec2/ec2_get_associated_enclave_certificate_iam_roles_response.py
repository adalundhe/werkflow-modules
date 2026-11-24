from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_associated_role import EC2AssociatedRole


class EC2GetAssociatedEnclaveCertificateIamRolesResponse(BaseModel):
    AssociatedRoles: list[EC2AssociatedRole] | None = None
    ResponseMetadata: dict[str, Any] | None = None
