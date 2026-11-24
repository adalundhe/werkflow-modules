from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionMediaAnalysisJobFailureDetails(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
