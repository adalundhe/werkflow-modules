from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeImageUsageReportEntriesRequest(BaseModel):
    ImageIds: list[StrictStr] | None = None
    ReportIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Filters: list[EC2FilterModel] | None = None
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
