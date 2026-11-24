from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_evaluation_acknowledgement_summary import ConnectEvaluationAcknowledgementSummary
from .connect_evaluation_contact_participant import ConnectEvaluationContactParticipant
from .connect_evaluation_score import ConnectEvaluationScore


class ConnectEvaluationSummary(BaseModel):
    EvaluationId: StrictStr | None = None
    EvaluationArn: StrictStr | None = None
    EvaluationFormTitle: StrictStr | None = None
    EvaluationFormId: StrictStr | None = None
    CalibrationSessionId: StrictStr | None = None
    Status: StrictStr | None = None
    AutoEvaluationEnabled: StrictBool | None = None
    AutoEvaluationStatus: StrictStr | None = None
    EvaluatorArn: StrictStr | None = None
    Score: ConnectEvaluationScore | None = None
    Acknowledgement: ConnectEvaluationAcknowledgementSummary | None = None
    EvaluationType: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ContactParticipant: ConnectEvaluationContactParticipant | None = None
