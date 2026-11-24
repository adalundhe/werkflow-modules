from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_data_query import EC2DataQuery


class EC2GetAwsNetworkPerformanceDataRequest(BaseModel):
    DataQueries: list[EC2DataQuery] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DryRun: StrictBool | None = None
