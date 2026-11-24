from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLookupTable(BaseModel):
    lookupTableArn: StrictStr | None = None
    lookupTableName: StrictStr | None = None
    description: StrictStr | None = None
    tableFields: list[StrictStr] | None = None
    recordsCount: StrictInt | None = None
    sizeBytes: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
    kmsKeyId: StrictStr | None = None
