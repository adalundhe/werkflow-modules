from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeImagesRequest(BaseModel):
    ExecutableUsers: list[StrictStr] | None = None
    ImageIds: list[StrictStr] | None = None
    Owners: list[StrictStr] | None = None
    IncludeDeprecated: StrictBool | None = None
    IncludeDisabled: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
