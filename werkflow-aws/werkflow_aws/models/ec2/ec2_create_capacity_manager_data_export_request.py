from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityManagerDataExportRequest(BaseModel):
    S3BucketName: StrictStr
    Schedule: Literal['hourly']
    OutputFormat: Literal['csv', 'parquet']
    S3BucketPrefix: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
