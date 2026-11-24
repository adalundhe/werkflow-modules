from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .transcribe_sync_redaction import TranscribeSyncRedaction


class TranscribeSyncItem(BaseModel):
    Id: StrictInt | None = None
    Content: StrictStr | None = None
    StartTime: StrictFloat | StrictInt | None = None
    EndTime: StrictFloat | StrictInt | None = None
    LanguageCode: StrictStr | None = None
    ChannelLabel: StrictStr | None = None
    SpeakerLabel: StrictStr | None = None
    VocabularyFilterMatch: StrictBool | None = None
    Redactions: list[TranscribeSyncRedaction] | None = None
