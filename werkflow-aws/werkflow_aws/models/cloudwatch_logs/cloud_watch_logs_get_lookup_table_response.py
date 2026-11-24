from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsGetLookupTableResponse(BaseModel):
    lookupTableArn: StrictStr | None = None
    lookupTableName: StrictStr | None = None
    description: StrictStr | None = None
    tableBody: StrictStr | None = None
    sizeBytes: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
    kmsKeyId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
