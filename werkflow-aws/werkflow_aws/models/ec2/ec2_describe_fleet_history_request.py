from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeFleetHistoryRequest(BaseModel):
    FleetId: StrictStr
    StartTime: datetime.datetime | StrictStr
    DryRun: StrictBool | None = None
    EventType: Literal['instance-change', 'fleet-change', 'service-error'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
