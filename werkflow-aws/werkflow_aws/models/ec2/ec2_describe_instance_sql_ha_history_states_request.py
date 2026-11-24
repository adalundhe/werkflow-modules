from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeInstanceSqlHaHistoryStatesRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filters: list[EC2FilterModel] | None = None
    DryRun: StrictBool | None = None
