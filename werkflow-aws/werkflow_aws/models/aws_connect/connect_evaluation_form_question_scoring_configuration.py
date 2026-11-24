from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .connect_evaluation_form_score_threshold import ConnectEvaluationFormScoreThreshold
from .connect_question_points_configuration import ConnectQuestionPointsConfiguration


class ConnectEvaluationFormQuestionScoringConfiguration(BaseModel):
    PointsConfiguration: ConnectQuestionPointsConfiguration | None = None
    IsExcludedFromScoring: StrictBool | None = None
    ScoreThresholds: list[ConnectEvaluationFormScoreThreshold] | None = None
