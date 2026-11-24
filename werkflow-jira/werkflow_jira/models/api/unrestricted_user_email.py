from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class UnrestrictedUserEmail(BaseModel):
    model_config = ConfigDict(extra="allow")

    accountId: StrictStr | None = None
    email: StrictStr | None = None
