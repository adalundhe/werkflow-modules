from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerReplicaRegionType(BaseModel):
    Region: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
