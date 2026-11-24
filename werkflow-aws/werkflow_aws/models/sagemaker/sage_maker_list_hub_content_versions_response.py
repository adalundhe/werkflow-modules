from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_hub_content_info import SageMakerHubContentInfo


class SageMakerListHubContentVersionsResponse(BaseModel):
    HubContentSummaries: list[SageMakerHubContentInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
