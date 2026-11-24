from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_replication_status_type import AWSSecretsManagerReplicationStatusType


class AWSSecretsManagerReplicateSecretToRegionsResponse(BaseModel):
    ARN: StrictStr | None = None
    ReplicationStatus: list[AWSSecretsManagerReplicationStatusType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
