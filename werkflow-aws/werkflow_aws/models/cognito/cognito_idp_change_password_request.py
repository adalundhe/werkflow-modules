from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPChangePasswordRequest(BaseModel):
    ProposedPassword: StrictStr
    AccessToken: StrictStr
    PreviousPassword: StrictStr | None = None
