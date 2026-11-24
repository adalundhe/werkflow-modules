from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeLaunchTemplateVersionsRequest(BaseModel):
    DryRun: StrictBool | None = None
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    Versions: list[StrictStr] | None = None
    MinVersion: StrictStr | None = None
    MaxVersion: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[EC2FilterModel] | None = None
    ResolveAlias: StrictBool | None = None
    IncludeManagedResources: StrictBool | None = None
