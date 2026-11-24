from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CognitoIDPUsernameConfigurationType(BaseModel):
    CaseSensitive: StrictBool | None = None
