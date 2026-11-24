from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendPiiOutputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
