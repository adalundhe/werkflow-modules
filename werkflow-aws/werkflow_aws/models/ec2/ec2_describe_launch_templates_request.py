from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeLaunchTemplatesRequest(BaseModel):
    DryRun: StrictBool | None = None
    LaunchTemplateIds: list[StrictStr] | None = None
    LaunchTemplateNames: list[StrictStr] | None = None
    Filters: list[EC2FilterModel] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    IncludeManagedResources: StrictBool | None = None
