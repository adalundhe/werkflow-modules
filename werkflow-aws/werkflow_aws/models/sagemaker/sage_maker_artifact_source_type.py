from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerArtifactSourceType(BaseModel):
    SourceIdType: StrictStr | None = None
    Value: StrictStr | None = None
