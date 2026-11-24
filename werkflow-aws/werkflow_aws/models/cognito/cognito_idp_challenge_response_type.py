from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPChallengeResponseType(BaseModel):
    ChallengeName: StrictStr | None = None
    ChallengeResponse: StrictStr | None = None
