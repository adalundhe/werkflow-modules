from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_run_execution_metrics_response import PinpointJourneyRunExecutionMetricsResponse


class PinpointGetJourneyRunExecutionMetricsResponse(BaseModel):
    JourneyRunExecutionMetricsResponse: PinpointJourneyRunExecutionMetricsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
