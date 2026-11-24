from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAuthChallengeRequestEvent(BaseModel):
    authorizationUrl: StrictStr | None = None
