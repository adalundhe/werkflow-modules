from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAuthorizedTargetsByService(BaseModel):
    Service: StrictStr | None = None
    AuthorizedTargets: list[StrictStr] | None = None
