from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeInstanceStatusRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    IncludeManagedResources: StrictBool | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    IncludeAllInstances: StrictBool | None = None
