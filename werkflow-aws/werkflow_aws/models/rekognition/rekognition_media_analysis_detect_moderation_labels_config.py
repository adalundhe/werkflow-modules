from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionMediaAnalysisDetectModerationLabelsConfig(BaseModel):
    MinConfidence: StrictFloat | StrictInt | None = None
    ProjectVersion: StrictStr | None = None
