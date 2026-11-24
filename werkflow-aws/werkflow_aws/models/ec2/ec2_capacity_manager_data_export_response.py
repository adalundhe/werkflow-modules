from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CapacityManagerDataExportResponse(BaseModel):
    CapacityManagerDataExportId: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3BucketPrefix: StrictStr | None = None
    Schedule: StrictStr | None = None
    OutputFormat: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LatestDeliveryStatus: StrictStr | None = None
    LatestDeliveryStatusMessage: StrictStr | None = None
    LatestDeliveryS3LocationUri: StrictStr | None = None
    LatestDeliveryTime: datetime.datetime | StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
