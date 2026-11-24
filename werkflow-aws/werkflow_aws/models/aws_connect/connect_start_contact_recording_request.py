from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_voice_recording_configuration import ConnectVoiceRecordingConfiguration


class ConnectStartContactRecordingRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    InitialContactId: StrictStr
    VoiceRecordingConfiguration: ConnectVoiceRecordingConfiguration
