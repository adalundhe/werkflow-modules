from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_score_threshold import ConnectEvaluationFormScoreThreshold


class ConnectEvaluationFormScoringStrategy(BaseModel):
    Mode: StrictStr | None = None
    Status: StrictStr | None = None
    ScoreThresholds: list[ConnectEvaluationFormScoreThreshold] | None = None
