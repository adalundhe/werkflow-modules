from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAssociatedStandard(BaseModel):
    StandardsId: StrictStr | None = None
