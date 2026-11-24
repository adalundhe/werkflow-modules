from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAuthChallengeResponseEvent(BaseModel):
    responseMap: dict[StrictStr, StrictStr]
