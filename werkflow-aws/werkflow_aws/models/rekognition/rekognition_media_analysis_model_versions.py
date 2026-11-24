from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionMediaAnalysisModelVersions(BaseModel):
    Moderation: StrictStr | None = None
