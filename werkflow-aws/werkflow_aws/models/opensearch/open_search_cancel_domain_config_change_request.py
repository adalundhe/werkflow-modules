from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchCancelDomainConfigChangeRequest(BaseModel):
    DomainName: StrictStr
    DryRun: StrictBool | None = None
