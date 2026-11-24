from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraServerSideEncryptionConfiguration(BaseModel):
    KmsKeyId: StrictStr | None = None
