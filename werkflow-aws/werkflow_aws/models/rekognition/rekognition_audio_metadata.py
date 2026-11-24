from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionAudioMetadata(BaseModel):
    Codec: StrictStr | None = None
    DurationMillis: StrictInt | None = None
    SampleRate: StrictInt | None = None
    NumberOfChannels: StrictInt | None = None
