from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowConnectorOAuthRequest(BaseModel):
    authCode: StrictStr | None = None
    redirectUri: StrictStr | None = None
    codeVerifier: StrictStr | None = None
