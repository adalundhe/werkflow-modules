from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class TranscribeSettings(BaseModel):
    VocabularyName: StrictStr | None = None
    ShowSpeakerLabels: StrictBool | None = None
    MaxSpeakerLabels: StrictInt | None = None
    ChannelIdentification: StrictBool | None = None
    ShowAlternatives: StrictBool | None = None
    MaxAlternatives: StrictInt | None = None
    VocabularyFilterName: StrictStr | None = None
    VocabularyFilterMethod: StrictStr | None = None
