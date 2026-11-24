from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_image_usage_resource_type_option import EC2ImageUsageResourceTypeOption


class EC2ImageUsageResourceType(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceTypeOptions: list[EC2ImageUsageResourceTypeOption] | None = None
