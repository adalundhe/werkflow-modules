from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_credentials import STSCredentials
from .sts_scoped_session import STSScopedSession


class STSGetScopedCredentialsResponse(BaseModel):
    Credentials: STSCredentials | None = None
    SessionInfo: STSScopedSession | None = None
    SessionTokenUtilization: StrictInt | None = None
    SessionTokenSize: StrictInt | None = None
    ScopedPoliciesCount: StrictInt | None = None
    SourceIdentity: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
