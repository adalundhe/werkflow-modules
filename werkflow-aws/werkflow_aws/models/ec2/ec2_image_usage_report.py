from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_image_usage_resource_type import EC2ImageUsageResourceType
from .ec2_tag_model import EC2TagModel


class EC2ImageUsageReport(BaseModel):
    ImageId: StrictStr | None = None
    ReportId: StrictStr | None = None
    ResourceTypes: list[EC2ImageUsageResourceType] | None = None
    AccountIds: list[StrictStr] | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
