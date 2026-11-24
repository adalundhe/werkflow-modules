from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectVoiceRecordingConfiguration(BaseModel):
    VoiceRecordingTrack: Literal['FROM_AGENT', 'TO_AGENT', 'ALL'] | None = None
    IvrRecordingTrack: Literal['ALL'] | None = None
