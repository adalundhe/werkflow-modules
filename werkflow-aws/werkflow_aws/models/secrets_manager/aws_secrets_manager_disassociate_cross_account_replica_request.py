from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerDisassociateCrossAccountReplicaRequest(BaseModel):
    SecretId: StrictStr
    CrossAccountReplicaARN: StrictStr
