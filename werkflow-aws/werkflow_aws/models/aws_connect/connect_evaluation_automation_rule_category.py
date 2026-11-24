from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_transcript_point_of_interest import ConnectEvaluationTranscriptPointOfInterest


class ConnectEvaluationAutomationRuleCategory(BaseModel):
    Category: StrictStr | None = None
    Condition: StrictStr | None = None
    PointsOfInterest: list[ConnectEvaluationTranscriptPointOfInterest] | None = None
