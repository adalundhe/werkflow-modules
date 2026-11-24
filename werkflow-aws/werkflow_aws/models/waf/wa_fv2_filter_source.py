from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2FilterSource(BaseModel):
    BotCategory: StrictStr | None = None
    BotOrganization: StrictStr | None = None
    BotName: StrictStr | None = None
