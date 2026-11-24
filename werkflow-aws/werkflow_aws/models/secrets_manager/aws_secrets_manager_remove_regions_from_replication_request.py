from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerRemoveRegionsFromReplicationRequest(BaseModel):
    SecretId: StrictStr
    RemoveReplicaRegions: list[StrictStr]
