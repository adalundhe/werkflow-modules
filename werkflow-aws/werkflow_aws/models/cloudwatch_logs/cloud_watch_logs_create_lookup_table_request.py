from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsCreateLookupTableRequest(BaseModel):
    lookupTableName: StrictStr
    description: StrictStr | None = None
    tableBody: StrictStr | None = None
    queryId: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
