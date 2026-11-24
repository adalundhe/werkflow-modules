from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAssociateSoftwareTokenRequest(BaseModel):
    AccessToken: StrictStr | None = None
    Session: StrictStr | None = None
