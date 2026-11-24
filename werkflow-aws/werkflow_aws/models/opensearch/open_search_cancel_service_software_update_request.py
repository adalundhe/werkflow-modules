from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCancelServiceSoftwareUpdateRequest(BaseModel):
    DomainName: StrictStr
