from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSMasterUserSecret(BaseModel):
    SecretArn: StrictStr | None = None
    SecretStatus: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
