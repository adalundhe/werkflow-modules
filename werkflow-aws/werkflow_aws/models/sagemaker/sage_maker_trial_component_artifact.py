from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrialComponentArtifact(BaseModel):
    MediaType: StrictStr | None = None
    Value: StrictStr | None = None
