from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_history_record import EC2HistoryRecord


class EC2DescribeSpotFleetRequestHistoryResponse(BaseModel):
    HistoryRecords: list[EC2HistoryRecord] | None = None
    LastEvaluatedTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    SpotFleetRequestId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
