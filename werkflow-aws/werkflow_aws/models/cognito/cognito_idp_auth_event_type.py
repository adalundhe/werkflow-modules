from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cognito_idp_challenge_response_type import CognitoIDPChallengeResponseType
from .cognito_idp_event_context_data_type import CognitoIDPEventContextDataType
from .cognito_idp_event_feedback_type import CognitoIDPEventFeedbackType
from .cognito_idp_event_risk_type import CognitoIDPEventRiskType


class CognitoIDPAuthEventType(BaseModel):
    EventId: StrictStr | None = None
    EventType: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    EventResponse: StrictStr | None = None
    EventRisk: CognitoIDPEventRiskType | None = None
    ChallengeResponses: list[CognitoIDPChallengeResponseType] | None = None
    EventContextData: CognitoIDPEventContextDataType | None = None
    EventFeedback: CognitoIDPEventFeedbackType | None = None
