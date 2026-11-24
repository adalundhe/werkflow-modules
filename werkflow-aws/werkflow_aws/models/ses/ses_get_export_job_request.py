from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetExportJobRequest(BaseModel):
    JobId: StrictStr
