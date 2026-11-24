from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_tag import TranscribeTag


class TranscribeTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[TranscribeTag]
