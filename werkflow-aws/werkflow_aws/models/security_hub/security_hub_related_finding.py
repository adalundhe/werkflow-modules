from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRelatedFinding(BaseModel):
    ProductArn: StrictStr | None = None
    Id: StrictStr | None = None
