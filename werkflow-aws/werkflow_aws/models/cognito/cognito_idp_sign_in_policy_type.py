from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPSignInPolicyType(BaseModel):
    AllowedFirstAuthFactors: list[StrictStr] | None = None
