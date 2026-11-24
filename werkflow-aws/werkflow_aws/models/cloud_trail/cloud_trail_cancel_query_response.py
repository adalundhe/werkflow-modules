from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailCancelQueryResponse(BaseModel):
    QueryId: StrictStr | None = None
    QueryStatus: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
