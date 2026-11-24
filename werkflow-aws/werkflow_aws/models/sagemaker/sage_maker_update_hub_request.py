from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateHubRequest(BaseModel):
    HubName: StrictStr
    HubDescription: StrictStr | None = None
    HubDisplayName: StrictStr | None = None
    HubSearchKeywords: list[StrictStr] | None = None
