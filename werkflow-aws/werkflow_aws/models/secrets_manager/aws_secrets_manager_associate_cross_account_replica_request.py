from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerAssociateCrossAccountReplicaRequest(BaseModel):
    SecretId: StrictStr
    CrossAccountReplicaARN: StrictStr
    ReplicaRestriction: Literal['SameOrg', 'NoRestriction'] | None = None
    ReplicationRoleARN: StrictStr | None = None
