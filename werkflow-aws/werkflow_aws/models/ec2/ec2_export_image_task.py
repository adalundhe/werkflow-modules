from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_export_task_s3_location import EC2ExportTaskS3Location
from .ec2_tag_model import EC2TagModel


class EC2ExportImageTask(BaseModel):
    Description: StrictStr | None = None
    ExportImageTaskId: StrictStr | None = None
    ImageId: StrictStr | None = None
    Progress: StrictStr | None = None
    S3ExportLocation: EC2ExportTaskS3Location | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
