from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeleteUtterancesRequest(BaseModel):
    botId: StrictStr
    localeId: StrictStr | None = None
    sessionId: StrictStr | None = None
