from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_credentials import STSCredentials


class STSAssumeRootResponse(BaseModel):
    Credentials: STSCredentials | None = None
    SourceIdentity: StrictStr | None = None
    SessionTokenUtilization: StrictInt | None = None
    SessionTokenSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
