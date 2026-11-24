from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_run_execution_activity_metrics_response import PinpointJourneyRunExecutionActivityMetricsResponse


class PinpointGetJourneyRunExecutionActivityMetricsResponse(BaseModel):
    JourneyRunExecutionActivityMetricsResponse: PinpointJourneyRunExecutionActivityMetricsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
