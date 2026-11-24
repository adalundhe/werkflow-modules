from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_date_range_kpi_response import PinpointJourneyDateRangeKpiResponse


class PinpointGetJourneyDateRangeKpiResponse(BaseModel):
    JourneyDateRangeKpiResponse: PinpointJourneyDateRangeKpiResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
