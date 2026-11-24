from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2AllowedPrincipal(BaseModel):
    PrincipalType: StrictStr | None = None
    Principal: StrictStr | None = None
    ServicePermissionId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ServiceId: StrictStr | None = None
    PermissionType: StrictStr | None = None
