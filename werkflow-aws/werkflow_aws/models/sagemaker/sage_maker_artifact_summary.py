from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_artifact_source import SageMakerArtifactSource


class SageMakerArtifactSummary(BaseModel):
    ArtifactArn: StrictStr | None = None
    ArtifactName: StrictStr | None = None
    Source: SageMakerArtifactSource | None = None
    ArtifactType: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
