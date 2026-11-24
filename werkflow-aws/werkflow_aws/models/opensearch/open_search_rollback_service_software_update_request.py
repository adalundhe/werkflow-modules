from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchRollbackServiceSoftwareUpdateRequest(BaseModel):
    DomainName: StrictStr
