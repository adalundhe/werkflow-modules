from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_ai_agent_input import ConnectAiAgentInput
from .connect_chat_message import ConnectChatMessage
from .connect_participant_details import ConnectParticipantDetails
from .connect_persistent_chat import ConnectPersistentChat


class ConnectStartAssistantContactRequest(BaseModel):
    InstanceId: StrictStr
    AiAgent: ConnectAiAgentInput
    ParticipantDetails: ConnectParticipantDetails
    InitialMessage: ConnectChatMessage | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
    PersistentChat: ConnectPersistentChat | None = None
    RelatedContactId: StrictStr | None = None
