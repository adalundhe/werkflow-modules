from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class ConnectEvaluationSearchMetadata(BaseModel):
    ContactId: StrictStr | None = None
    EvaluatorArn: StrictStr | None = None
    ContactAgentId: StrictStr | None = None
    CalibrationSessionId: StrictStr | None = None
    ScorePercentage: StrictFloat | StrictInt | None = None
    ScoreAutomaticFail: StrictBool | None = None
    ScoreNotApplicable: StrictBool | None = None
    AutoEvaluationEnabled: StrictBool | None = None
    AutoEvaluationStatus: StrictStr | None = None
    AcknowledgedTime: datetime.datetime | StrictStr | None = None
    AcknowledgedBy: StrictStr | None = None
    AcknowledgerComment: StrictStr | None = None
    SamplingJobId: StrictStr | None = None
    ReviewId: StrictStr | None = None
    ContactParticipantRole: StrictStr | None = None
    ContactParticipantId: StrictStr | None = None
    EarnedPoints: StrictInt | None = None
    MaxBasePoint: StrictInt | None = None
    PerformanceCategory: StrictStr | None = None
