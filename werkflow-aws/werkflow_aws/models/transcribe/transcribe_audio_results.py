from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_sync_item import TranscribeSyncItem


class TranscribeAudioResults(BaseModel):
    Transcript: StrictStr | None = None
    Items: list[TranscribeSyncItem] | None = None
