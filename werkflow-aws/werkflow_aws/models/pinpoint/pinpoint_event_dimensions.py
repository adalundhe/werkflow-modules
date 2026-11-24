from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_attribute_dimension import PinpointAttributeDimension
from .pinpoint_metric_dimension import PinpointMetricDimension
from .pinpoint_set_dimension import PinpointSetDimension


class PinpointEventDimensions(BaseModel):
    Attributes: dict[StrictStr, PinpointAttributeDimension] | None = None
    EventType: PinpointSetDimension | None = None
    Metrics: dict[StrictStr, PinpointMetricDimension] | None = None
