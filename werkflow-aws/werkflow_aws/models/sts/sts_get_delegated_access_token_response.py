from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_credentials import STSCredentials


class STSGetDelegatedAccessTokenResponse(BaseModel):
    Credentials: STSCredentials | None = None
    PackedPolicySize: StrictInt | None = None
    AssumedPrincipal: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
