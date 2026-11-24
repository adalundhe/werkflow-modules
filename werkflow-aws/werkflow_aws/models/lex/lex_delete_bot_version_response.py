from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteBotVersionResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    botStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
