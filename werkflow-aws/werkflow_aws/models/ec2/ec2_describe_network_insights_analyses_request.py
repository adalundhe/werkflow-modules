from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeNetworkInsightsAnalysesRequest(BaseModel):
    NetworkInsightsAnalysisIds: list[StrictStr] | None = None
    NetworkInsightsPathId: StrictStr | None = None
    AnalysisStartTime: datetime.datetime | StrictStr | None = None
    AnalysisEndTime: datetime.datetime | StrictStr | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
