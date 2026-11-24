from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESCancelExportJobRequest(BaseModel):
    JobId: StrictStr
