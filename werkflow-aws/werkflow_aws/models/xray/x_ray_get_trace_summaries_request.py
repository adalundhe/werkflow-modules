from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_sampling_strategy import XRaySamplingStrategy


class XRayGetTraceSummariesRequest(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    TimeRangeType: Literal['TraceId', 'Event', 'Service'] | None = None
    Sampling: StrictBool | None = None
    SamplingStrategy: XRaySamplingStrategy | None = None
    FilterExpression: StrictStr | None = None
    NextToken: StrictStr | None = None
