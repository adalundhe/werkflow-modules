from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDeleteJobRequest(BaseModel):
    jobId: StrictStr
    force: StrictBool | None = None
    namespaceId: StrictStr | None = None
