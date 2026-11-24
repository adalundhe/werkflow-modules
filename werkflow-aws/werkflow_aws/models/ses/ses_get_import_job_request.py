from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetImportJobRequest(BaseModel):
    JobId: StrictStr
