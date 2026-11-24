from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerCancelRotateSecretResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    VersionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
