from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class UpdateUserToGroupBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    accountId: StrictStr | None = None
    name: StrictStr | None = None
