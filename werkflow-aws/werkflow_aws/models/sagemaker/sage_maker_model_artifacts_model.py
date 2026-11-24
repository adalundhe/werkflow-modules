from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelArtifactsModel(BaseModel):
    S3ModelArtifacts: StrictStr | None = None
