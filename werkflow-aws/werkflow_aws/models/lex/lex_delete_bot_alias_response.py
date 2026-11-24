from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexDeleteBotAliasResponse(BaseModel):
    botAliasId: StrictStr | None = None
    botId: StrictStr | None = None
    botAliasStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
