from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_image_usage_resource_type_request import EC2ImageUsageResourceTypeRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateImageUsageReportRequest(BaseModel):
    ImageId: StrictStr
    ResourceTypes: list[EC2ImageUsageResourceTypeRequest]
    DryRun: StrictBool | None = None
    AccountIds: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
