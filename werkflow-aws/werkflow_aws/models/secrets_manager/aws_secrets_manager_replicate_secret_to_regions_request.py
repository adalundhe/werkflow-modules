from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .aws_secrets_manager_replica_region_type import AWSSecretsManagerReplicaRegionType


class AWSSecretsManagerReplicateSecretToRegionsRequest(BaseModel):
    SecretId: StrictStr
    AddReplicaRegions: list[AWSSecretsManagerReplicaRegionType]
    ForceOverwriteReplicaSecret: StrictBool | None = None
