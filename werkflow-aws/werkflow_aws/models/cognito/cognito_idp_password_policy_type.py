from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class CognitoIDPPasswordPolicyType(BaseModel):
    MinimumLength: StrictInt | None = None
    RequireUppercase: StrictBool | None = None
    RequireLowercase: StrictBool | None = None
    RequireNumbers: StrictBool | None = None
    RequireSymbols: StrictBool | None = None
    PasswordHistorySize: StrictInt | None = None
    TemporaryPasswordValidityDays: StrictInt | None = None
