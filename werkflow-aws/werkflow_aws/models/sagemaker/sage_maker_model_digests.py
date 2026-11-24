from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelDigests(BaseModel):
    ArtifactDigest: StrictStr | None = None
