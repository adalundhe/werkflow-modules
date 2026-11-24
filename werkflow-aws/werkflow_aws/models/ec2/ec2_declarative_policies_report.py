from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2DeclarativePoliciesReport(BaseModel):
    ReportId: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3Prefix: StrictStr | None = None
    TargetId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
