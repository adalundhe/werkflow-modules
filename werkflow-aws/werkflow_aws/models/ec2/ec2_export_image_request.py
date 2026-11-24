from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_export_task_s3_location_request import EC2ExportTaskS3LocationRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2ExportImageRequest(BaseModel):
    DiskImageFormat: Literal['VMDK', 'RAW', 'VHD']
    ImageId: StrictStr
    S3ExportLocation: EC2ExportTaskS3LocationRequest
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    RoleName: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
