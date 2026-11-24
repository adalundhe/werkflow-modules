from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseToOCSF(BaseModel):
    source: StrictStr | None = None
    eventSource: StrictStr | None = None
    ocsfVersion: StrictStr | None = None
    mappingVersion: StrictStr | None = None
