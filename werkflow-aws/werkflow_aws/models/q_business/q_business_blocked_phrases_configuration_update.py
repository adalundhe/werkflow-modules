from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessBlockedPhrasesConfigurationUpdate(BaseModel):
    blockedPhrasesToCreateOrUpdate: list[StrictStr] | None = None
    blockedPhrasesToDelete: list[StrictStr] | None = None
    systemMessageOverride: StrictStr | None = None
