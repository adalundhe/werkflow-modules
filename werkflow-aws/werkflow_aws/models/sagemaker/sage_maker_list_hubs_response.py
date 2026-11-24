from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_info import SageMakerHubInfo


class SageMakerListHubsResponse(BaseModel):
    HubSummaries: list[SageMakerHubInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
