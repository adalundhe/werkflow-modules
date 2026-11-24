from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_history_record_entry import EC2HistoryRecordEntry


class EC2DescribeFleetHistoryResponse(BaseModel):
    HistoryRecords: list[EC2HistoryRecordEntry] | None = None
    LastEvaluatedTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    FleetId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
