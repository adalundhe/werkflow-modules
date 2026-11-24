from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelArtifacts(BaseModel):
    S3ModelArtifacts: StrictStr | None = None
