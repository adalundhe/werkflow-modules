from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKBatchDisassociateScramSecretRequest(BaseModel):
    ClusterArn: StrictStr
    SecretArnList: list[StrictStr]
