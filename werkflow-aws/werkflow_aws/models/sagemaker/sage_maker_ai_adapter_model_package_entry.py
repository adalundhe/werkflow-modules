from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIAdapterModelPackageEntry(BaseModel):
    AdapterId: StrictStr | None = None
    ModelPackageArn: StrictStr | None = None
