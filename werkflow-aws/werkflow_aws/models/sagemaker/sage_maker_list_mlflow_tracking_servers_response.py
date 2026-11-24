from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_tracking_server_summary import SageMakerTrackingServerSummary


class SageMakerListMlflowTrackingServersResponse(BaseModel):
    TrackingServerSummaries: list[SageMakerTrackingServerSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
