from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_session_credentials import AWSS3SessionCredentials


class AWSS3CreateSessionResponse(BaseModel):
    ServerSideEncryption: StrictStr | None = None
    SSEKMSKeyId: StrictStr | None = None
    SSEKMSEncryptionContext: StrictStr | None = None
    BucketKeyEnabled: StrictBool | None = None
    Credentials: AWSS3SessionCredentials | None = None
    ResponseMetadata: dict[str, Any] | None = None
