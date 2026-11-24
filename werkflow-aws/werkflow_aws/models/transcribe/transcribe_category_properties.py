from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .transcribe_rule import TranscribeRule
from .transcribe_tag import TranscribeTag


class TranscribeCategoryProperties(BaseModel):
    CategoryName: StrictStr | None = None
    Rules: list[TranscribeRule] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    Tags: list[TranscribeTag] | None = None
    InputType: StrictStr | None = None
