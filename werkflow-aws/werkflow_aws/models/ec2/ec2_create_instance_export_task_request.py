from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ec2_export_to_s3_task_specification import EC2ExportToS3TaskSpecification
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateInstanceExportTaskRequest(BaseModel):
    InstanceId: StrictStr
    TargetEnvironment: Literal['citrix', 'vmware', 'microsoft']
    ExportToS3Task: EC2ExportToS3TaskSpecification
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    Description: StrictStr | None = None
