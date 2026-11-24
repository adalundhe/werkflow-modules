from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_artifact_source import SageMakerArtifactSource


class SageMakerDeleteArtifactRequest(BaseModel):
    ArtifactArn: StrictStr | None = None
    Source: SageMakerArtifactSource | None = None
