from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_application_date_range_kpi_response import PinpointApplicationDateRangeKpiResponse


class PinpointGetApplicationDateRangeKpiResponse(BaseModel):
    ApplicationDateRangeKpiResponse: PinpointApplicationDateRangeKpiResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
