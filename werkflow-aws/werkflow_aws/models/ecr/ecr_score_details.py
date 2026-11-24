from __future__ import annotations
from pydantic import BaseModel
from .ecr_cvss_score_details import ECRCvssScoreDetails


class ECRScoreDetails(BaseModel):
    cvss: ECRCvssScoreDetails | None = None
