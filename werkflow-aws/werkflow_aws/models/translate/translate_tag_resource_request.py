from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_tag import TranslateTag


class TranslateTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[TranslateTag]
