from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetLookupTableRequest(BaseModel):
    lookupTableArn: StrictStr
