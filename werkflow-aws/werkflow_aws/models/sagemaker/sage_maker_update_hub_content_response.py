from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerUpdateHubContentResponse(BaseModel):
    HubArn: StrictStr | None = None
    HubContentArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
