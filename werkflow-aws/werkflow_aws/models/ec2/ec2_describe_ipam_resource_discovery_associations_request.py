from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeIpamResourceDiscoveryAssociationsRequest(BaseModel):
    DryRun: StrictBool | None = None
    IpamResourceDiscoveryAssociationIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[EC2FilterModel] | None = None
