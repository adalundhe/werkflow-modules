from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_image_usage_resource_type_option_request import EC2ImageUsageResourceTypeOptionRequest


class EC2ImageUsageResourceTypeRequest(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceTypeOptions: list[EC2ImageUsageResourceTypeOptionRequest] | None = None
