from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_load_permission_modifications import EC2LoadPermissionModifications


class EC2ModifyFpgaImageAttributeRequest(BaseModel):
    FpgaImageId: StrictStr
    DryRun: StrictBool | None = None
    Attribute: Literal['description', 'name', 'loadPermission', 'productCodes'] | None = None
    OperationType: Literal['add', 'remove'] | None = None
    UserIds: list[StrictStr] | None = None
    UserGroups: list[StrictStr] | None = None
    ProductCodes: list[StrictStr] | None = None
    LoadPermission: EC2LoadPermissionModifications | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
