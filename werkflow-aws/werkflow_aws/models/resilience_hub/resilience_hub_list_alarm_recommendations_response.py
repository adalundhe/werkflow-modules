from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_alarm_recommendation import ResilienceHubAlarmRecommendation


class ResilienceHubListAlarmRecommendationsResponse(BaseModel):
    alarmRecommendations: list[ResilienceHubAlarmRecommendation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
