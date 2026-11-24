from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdgePresetDeploymentOutput(BaseModel):
    Type: StrictStr | None = None
    Artifact: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
