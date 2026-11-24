from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsCreateLookupTableResponse(BaseModel):
    lookupTableArn: StrictStr | None = None
    createdAt: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
