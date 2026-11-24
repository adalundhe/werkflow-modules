from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailGenerateQueryResponse(BaseModel):
    QueryStatement: StrictStr | None = None
    QueryAlias: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
