from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeHttpParameters(BaseModel):
    PathParameterValues: list[StrictStr] | None = None
    HeaderParameters: dict[StrictStr, StrictStr] | None = None
    QueryStringParameters: dict[StrictStr, StrictStr] | None = None
