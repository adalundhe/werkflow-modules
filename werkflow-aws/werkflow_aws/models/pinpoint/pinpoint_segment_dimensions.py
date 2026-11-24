from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_attribute_dimension import PinpointAttributeDimension
from .pinpoint_metric_dimension import PinpointMetricDimension
from .pinpoint_segment_behaviors import PinpointSegmentBehaviors
from .pinpoint_segment_demographics import PinpointSegmentDemographics
from .pinpoint_segment_location import PinpointSegmentLocation


class PinpointSegmentDimensions(BaseModel):
    Attributes: dict[StrictStr, PinpointAttributeDimension] | None = None
    Behavior: PinpointSegmentBehaviors | None = None
    Demographic: PinpointSegmentDemographics | None = None
    Location: PinpointSegmentLocation | None = None
    Metrics: dict[StrictStr, PinpointMetricDimension] | None = None
    UserAttributes: dict[StrictStr, PinpointAttributeDimension] | None = None
