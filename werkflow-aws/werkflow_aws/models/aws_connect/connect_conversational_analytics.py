from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_analysis_reference_state import ConnectContactAnalysisReferenceState
from .connect_conversational_analytics_configuration import ConnectConversationalAnalyticsConfiguration


class ConnectConversationalAnalytics(BaseModel):
    Configuration: ConnectConversationalAnalyticsConfiguration | None = None
    ContactAnalysisReferenceState: ConnectContactAnalysisReferenceState | None = None
