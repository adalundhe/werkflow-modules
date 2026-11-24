from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_export_to_s3_task import EC2ExportToS3Task
from .ec2_instance_export_details import EC2InstanceExportDetails
from .ec2_tag_model import EC2TagModel


class EC2ExportTask(BaseModel):
    Description: StrictStr | None = None
    ExportTaskId: StrictStr | None = None
    ExportToS3Task: EC2ExportToS3Task | None = None
    InstanceExportDetails: EC2InstanceExportDetails | None = None
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
