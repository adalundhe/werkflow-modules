from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class StatusMigration(BaseModel):
    model_config = ConfigDict(extra="allow")

    newStatusReference: StrictStr | None = None
    oldStatusReference: StrictStr | None = None
