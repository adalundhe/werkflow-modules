from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTGetJobDocumentRequest(BaseModel):
    jobId: StrictStr
    beforeSubstitution: StrictBool | None = None
