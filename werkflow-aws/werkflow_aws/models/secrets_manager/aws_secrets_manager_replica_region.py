from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerReplicaRegion(BaseModel):
    Region: StrictStr
    KmsKeyId: StrictStr | None = None
