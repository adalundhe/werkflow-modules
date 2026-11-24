from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAuthChallengeResponse(BaseModel):
    responseMap: dict[StrictStr, StrictStr]
