from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class TranscribeMedicalTranscriptionSetting(BaseModel):
    ShowSpeakerLabels: StrictBool | None = None
    MaxSpeakerLabels: StrictInt | None = None
    ChannelIdentification: StrictBool | None = None
    ShowAlternatives: StrictBool | None = None
    MaxAlternatives: StrictInt | None = None
    VocabularyName: StrictStr | None = None
