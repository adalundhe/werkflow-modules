from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CognitoIDPEmailMfaSettingsType(BaseModel):
    Enabled: StrictBool | None = None
    PreferredMfa: StrictBool | None = None
