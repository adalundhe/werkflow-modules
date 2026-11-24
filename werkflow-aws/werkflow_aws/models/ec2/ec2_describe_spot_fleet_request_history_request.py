from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeSpotFleetRequestHistoryRequest(BaseModel):
    SpotFleetRequestId: StrictStr
    StartTime: datetime.datetime | StrictStr
    DryRun: StrictBool | None = None
    EventType: Literal['instanceChange', 'fleetRequestChange', 'error', 'information'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
