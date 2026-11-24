from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_request_ipam_resource_tag import EC2RequestIpamResourceTag


class EC2ModifyIpamPoolRequest(BaseModel):
    IpamPoolId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    AutoImport: StrictBool | None = None
    AllocationMinNetmaskLength: StrictInt | None = None
    AllocationMaxNetmaskLength: StrictInt | None = None
    AllocationDefaultNetmaskLength: StrictInt | None = None
    ClearAllocationDefaultNetmaskLength: StrictBool | None = None
    AddAllocationResourceTags: list[EC2RequestIpamResourceTag] | None = None
    RemoveAllocationResourceTags: list[EC2RequestIpamResourceTag] | None = None
