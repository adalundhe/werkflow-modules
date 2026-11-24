from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIAdapterS3Entry(BaseModel):
    AdapterId: StrictStr | None = None
    S3Uri: StrictStr | None = None
