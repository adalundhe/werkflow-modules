from __future__ import annotations
from pydantic import BaseModel
from .connect_search_contacts_time_range import ConnectSearchContactsTimeRange
from .connect_search_contacts_timestamp_condition import ConnectSearchContactsTimestampCondition


class ConnectSearchContactsAdditionalTimeRangeCriteria(BaseModel):
    TimeRange: ConnectSearchContactsTimeRange | None = None
    TimestampCondition: ConnectSearchContactsTimestampCondition | None = None
