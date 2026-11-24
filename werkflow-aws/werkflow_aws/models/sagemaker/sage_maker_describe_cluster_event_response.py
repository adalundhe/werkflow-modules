from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_cluster_event_detail import SageMakerClusterEventDetail


class SageMakerDescribeClusterEventResponse(BaseModel):
    EventDetails: SageMakerClusterEventDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
