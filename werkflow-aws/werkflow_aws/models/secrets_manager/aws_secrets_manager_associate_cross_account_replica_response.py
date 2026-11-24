from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerAssociateCrossAccountReplicaResponse(BaseModel):
    ARN: StrictStr | None = None
    CrossAccountReplicaARN: StrictStr | None = None
    ReplicationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
