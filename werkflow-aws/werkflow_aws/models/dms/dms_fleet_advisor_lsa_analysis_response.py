from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSFleetAdvisorLsaAnalysisResponse(BaseModel):
    LsaAnalysisId: StrictStr | None = None
    Status: StrictStr | None = None
