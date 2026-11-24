from __future__ import annotations
from pydantic import BaseModel
from .connect_chat_contact_metrics import ConnectChatContactMetrics
from .connect_participant_metrics import ConnectParticipantMetrics


class ConnectChatMetrics(BaseModel):
    ChatContactMetrics: ConnectChatContactMetrics | None = None
    AgentMetrics: ConnectParticipantMetrics | None = None
    CustomerMetrics: ConnectParticipantMetrics | None = None
