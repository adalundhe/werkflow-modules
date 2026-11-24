from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_cluster_event_summary import SageMakerClusterEventSummary


class SageMakerListClusterEventsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Events: list[SageMakerClusterEventSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
