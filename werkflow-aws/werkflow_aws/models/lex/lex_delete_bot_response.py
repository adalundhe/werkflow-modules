from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteBotResponse(BaseModel):
    botId: StrictStr | None = None
    botStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
