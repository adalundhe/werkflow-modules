from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAssociationStateDetails(BaseModel):
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
