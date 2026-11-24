from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFileSource(BaseModel):
    ContentType: StrictStr | None = None
    ContentDigest: StrictStr | None = None
    S3Uri: StrictStr | None = None
