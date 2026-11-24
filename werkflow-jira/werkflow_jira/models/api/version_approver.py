from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class VersionApprover(BaseModel):
    model_config = ConfigDict(extra="allow")

    accountId: StrictStr | None = None
    declineReason: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
