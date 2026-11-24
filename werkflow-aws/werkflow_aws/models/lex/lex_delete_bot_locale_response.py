from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteBotLocaleResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botLocaleStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
