from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BatchUpdateServiceJobResponse(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    jobId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
