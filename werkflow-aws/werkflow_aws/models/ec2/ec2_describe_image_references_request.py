from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_resource_type_request import EC2ResourceTypeRequest


class EC2DescribeImageReferencesRequest(BaseModel):
    ImageIds: list[StrictStr]
    IncludeAllResourceTypes: StrictBool | None = None
    ResourceTypes: list[EC2ResourceTypeRequest] | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
