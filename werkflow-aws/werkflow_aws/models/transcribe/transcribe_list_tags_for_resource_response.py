from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_tag import TranscribeTag


class TranscribeListTagsForResourceResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    Tags: list[TranscribeTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
