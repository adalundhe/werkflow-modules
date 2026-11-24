from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateArtifactRequest(BaseModel):
    ArtifactArn: StrictStr
    ArtifactName: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    PropertiesToRemove: list[StrictStr] | None = None
