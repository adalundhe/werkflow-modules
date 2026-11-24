from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailStartQueryResponse(BaseModel):
    QueryId: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
