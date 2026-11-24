from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataSyncStartTaskExecutionResponse(BaseModel):
    TaskExecutionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
