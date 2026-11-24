from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCancelJobResponse(BaseModel):
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
