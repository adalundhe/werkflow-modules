from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CognitoIDPWebAuthnMfaSettingsType(BaseModel):
    Enabled: StrictBool | None = None
