from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_collector_response import DMSCollectorResponse


class DMSDescribeFleetAdvisorCollectorsResponse(BaseModel):
    Collectors: list[DMSCollectorResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
