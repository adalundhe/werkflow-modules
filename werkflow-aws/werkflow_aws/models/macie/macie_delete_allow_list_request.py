from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDeleteAllowListRequest(BaseModel):
    id: StrictStr
    ignoreJobChecks: StrictStr | None = None
