from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKEncryptionConfiguration(BaseModel):
    KmsKeyArn: StrictStr | None = None
