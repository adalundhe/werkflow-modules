from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_execution_activity_metrics_response import PinpointJourneyExecutionActivityMetricsResponse


class PinpointGetJourneyExecutionActivityMetricsResponse(BaseModel):
    JourneyExecutionActivityMetricsResponse: PinpointJourneyExecutionActivityMetricsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
