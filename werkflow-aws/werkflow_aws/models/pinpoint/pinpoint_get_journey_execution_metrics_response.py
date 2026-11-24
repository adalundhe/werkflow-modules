from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_execution_metrics_response import PinpointJourneyExecutionMetricsResponse


class PinpointGetJourneyExecutionMetricsResponse(BaseModel):
    JourneyExecutionMetricsResponse: PinpointJourneyExecutionMetricsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
