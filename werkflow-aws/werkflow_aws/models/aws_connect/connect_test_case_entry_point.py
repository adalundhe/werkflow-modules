from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_chat_entry_point_parameters import ConnectChatEntryPointParameters
from .connect_voice_call_entry_point_parameters import ConnectVoiceCallEntryPointParameters


class ConnectTestCaseEntryPoint(BaseModel):
    Type: StrictStr | None = None
    VoiceCallEntryPointParameters: ConnectVoiceCallEntryPointParameters | None = None
    ChatEntryPointParameters: ConnectChatEntryPointParameters | None = None
