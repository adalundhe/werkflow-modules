from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AWSSecretsManagerGetRandomPasswordRequest(BaseModel):
    PasswordLength: StrictInt | None = None
    ExcludeCharacters: StrictStr | None = None
    ExcludeNumbers: StrictBool | None = None
    ExcludePunctuation: StrictBool | None = None
    ExcludeUppercase: StrictBool | None = None
    ExcludeLowercase: StrictBool | None = None
    IncludeSpace: StrictBool | None = None
    RequireEachIncludedType: StrictBool | None = None
