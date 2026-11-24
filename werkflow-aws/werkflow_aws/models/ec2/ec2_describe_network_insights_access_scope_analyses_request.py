from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeNetworkInsightsAccessScopeAnalysesRequest(BaseModel):
    NetworkInsightsAccessScopeAnalysisIds: list[StrictStr] | None = None
    NetworkInsightsAccessScopeId: StrictStr | None = None
    AnalysisStartTimeBegin: datetime.datetime | StrictStr | None = None
    AnalysisStartTimeEnd: datetime.datetime | StrictStr | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
