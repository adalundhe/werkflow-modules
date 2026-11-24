from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class IAMPasswordPolicy(BaseModel):
    MinimumPasswordLength: StrictInt | None = None
    RequireSymbols: StrictBool | None = None
    RequireNumbers: StrictBool | None = None
    RequireUppercaseCharacters: StrictBool | None = None
    RequireLowercaseCharacters: StrictBool | None = None
    AllowUsersToChangePassword: StrictBool | None = None
    ExpirePasswords: StrictBool | None = None
    MaxPasswordAge: StrictInt | None = None
    PasswordReusePrevention: StrictInt | None = None
    HardExpiry: StrictBool | None = None
