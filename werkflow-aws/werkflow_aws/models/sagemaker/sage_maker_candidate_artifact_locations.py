from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCandidateArtifactLocations(BaseModel):
    Explainability: StrictStr | None = None
    ModelInsights: StrictStr | None = None
    BacktestResults: StrictStr | None = None
