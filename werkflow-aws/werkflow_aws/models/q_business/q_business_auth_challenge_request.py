from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAuthChallengeRequest(BaseModel):
    authorizationUrl: StrictStr | None = None
