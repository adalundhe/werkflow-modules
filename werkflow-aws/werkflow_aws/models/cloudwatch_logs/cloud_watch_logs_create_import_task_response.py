from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsCreateImportTaskResponse(BaseModel):
    importId: StrictStr | None = None
    importDestinationArn: StrictStr | None = None
    creationTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
