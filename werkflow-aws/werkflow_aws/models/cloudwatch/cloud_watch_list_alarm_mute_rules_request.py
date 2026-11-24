from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchListAlarmMuteRulesRequest(BaseModel):
    AlarmName: StrictStr | None = None
    Statuses: list[Literal['SCHEDULED', 'ACTIVE', 'EXPIRED']] | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
