from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ecr_cvss_score_adjustment import ECRCvssScoreAdjustment


class ECRCvssScoreDetails(BaseModel):
    adjustments: list[ECRCvssScoreAdjustment] | None = None
    score: StrictFloat | StrictInt | None = None
    scoreSource: StrictStr | None = None
    scoringVector: StrictStr | None = None
    version: StrictStr | None = None
