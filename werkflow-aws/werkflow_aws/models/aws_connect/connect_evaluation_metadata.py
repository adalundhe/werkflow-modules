from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_auto_evaluation_details import ConnectAutoEvaluationDetails
from .connect_evaluation_acknowledgement import ConnectEvaluationAcknowledgement
from .connect_evaluation_contact_participant import ConnectEvaluationContactParticipant
from .connect_evaluation_review_metadata import ConnectEvaluationReviewMetadata
from .connect_evaluation_score import ConnectEvaluationScore


class ConnectEvaluationMetadata(BaseModel):
    ContactId: StrictStr | None = None
    EvaluatorArn: StrictStr | None = None
    ContactAgentId: StrictStr | None = None
    CalibrationSessionId: StrictStr | None = None
    Score: ConnectEvaluationScore | None = None
    AutoEvaluation: ConnectAutoEvaluationDetails | None = None
    Acknowledgement: ConnectEvaluationAcknowledgement | None = None
    Review: ConnectEvaluationReviewMetadata | None = None
    ContactParticipant: ConnectEvaluationContactParticipant | None = None
    SamplingJobId: StrictStr | None = None
