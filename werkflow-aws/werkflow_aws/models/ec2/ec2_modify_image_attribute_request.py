from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_attribute_value import EC2AttributeValue
from .ec2_launch_permission_modifications import EC2LaunchPermissionModifications


class EC2ModifyImageAttributeRequest(BaseModel):
    ImageId: StrictStr
    Attribute: StrictStr | None = None
    Description: EC2AttributeValue | None = None
    LaunchPermission: EC2LaunchPermissionModifications | None = None
    OperationType: Literal['add', 'remove'] | None = None
    ProductCodes: list[StrictStr] | None = None
    UserGroups: list[StrictStr] | None = None
    UserIds: list[StrictStr] | None = None
    Value: StrictStr | None = None
    OrganizationArns: list[StrictStr] | None = None
    OrganizationalUnitArns: list[StrictStr] | None = None
    ImdsSupport: EC2AttributeValue | None = None
    DryRun: StrictBool | None = None
