from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_trail_lookup_attribute import CloudTrailLookupAttribute


class CloudTrailLookupEventsRequest(BaseModel):
    LookupAttributes: list[CloudTrailLookupAttribute] | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    EventCategory: Literal['insight'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
