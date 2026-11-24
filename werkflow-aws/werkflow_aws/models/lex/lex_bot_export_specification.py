from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBotExportSpecification(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
