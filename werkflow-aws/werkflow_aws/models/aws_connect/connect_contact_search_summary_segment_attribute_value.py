from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_segment_attribute_value import ConnectSegmentAttributeValue


class ConnectContactSearchSummarySegmentAttributeValue(BaseModel):
    ValueString: StrictStr | None = None
    ValueMap: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
