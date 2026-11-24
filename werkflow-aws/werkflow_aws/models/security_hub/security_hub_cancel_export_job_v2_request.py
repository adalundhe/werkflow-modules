from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCancelExportJobV2Request(BaseModel):
    ExportJobId: StrictStr
