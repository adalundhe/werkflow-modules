from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetExportJobV2Request(BaseModel):
    ExportJobId: StrictStr
