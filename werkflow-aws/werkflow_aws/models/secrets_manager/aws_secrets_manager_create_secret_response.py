from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_replication_status import AWSSecretsManagerReplicationStatus


class AWSSecretsManagerCreateSecretResponse(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    VersionId: StrictStr | None = None
    ReplicationStatus: list[AWSSecretsManagerReplicationStatus] | None = None
