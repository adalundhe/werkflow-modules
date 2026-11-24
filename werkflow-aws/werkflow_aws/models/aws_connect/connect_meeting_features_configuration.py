from __future__ import annotations
from pydantic import BaseModel
from .connect_audio_features import ConnectAudioFeatures


class ConnectMeetingFeaturesConfiguration(BaseModel):
    Audio: ConnectAudioFeatures | None = None
