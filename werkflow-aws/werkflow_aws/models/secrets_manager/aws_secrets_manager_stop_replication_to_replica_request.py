from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerStopReplicationToReplicaRequest(BaseModel):
    SecretId: StrictStr
