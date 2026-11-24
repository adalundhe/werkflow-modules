from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeNetworkInterfacePermissionsRequest(BaseModel):
    NetworkInterfacePermissionIds: list[StrictStr] | None = None
    Filters: list[EC2FilterModel] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
