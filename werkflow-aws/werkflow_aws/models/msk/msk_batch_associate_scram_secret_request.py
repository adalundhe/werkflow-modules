from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKBatchAssociateScramSecretRequest(BaseModel):
    ClusterArn: StrictStr
    SecretArnList: list[StrictStr]
