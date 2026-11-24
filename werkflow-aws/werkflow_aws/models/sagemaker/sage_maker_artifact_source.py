from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_artifact_source_type import SageMakerArtifactSourceType


class SageMakerArtifactSource(BaseModel):
    SourceUri: StrictStr | None = None
    SourceTypes: list[SageMakerArtifactSourceType] | None = None
