from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerDisassociateCrossAccountReplicaResponse(BaseModel):
    ARN: StrictStr | None = None
    CrossAccountReplicaARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
