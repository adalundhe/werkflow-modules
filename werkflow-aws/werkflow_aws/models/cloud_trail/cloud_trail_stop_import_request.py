from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStopImportRequest(BaseModel):
    ImportId: StrictStr
