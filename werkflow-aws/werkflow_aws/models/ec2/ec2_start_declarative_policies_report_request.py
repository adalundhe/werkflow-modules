from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2StartDeclarativePoliciesReportRequest(BaseModel):
    S3Bucket: StrictStr
    TargetId: StrictStr
    DryRun: StrictBool | None = None
    S3Prefix: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
