from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsUpdateLookupTableRequest(BaseModel):
    lookupTableArn: StrictStr
    description: StrictStr | None = None
    tableBody: StrictStr | None = None
    queryId: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
