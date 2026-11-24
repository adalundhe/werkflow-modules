from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCancelJobRequest(BaseModel):
    jobId: StrictStr
    reasonCode: StrictStr | None = None
    comment: StrictStr | None = None
    force: StrictBool | None = None
