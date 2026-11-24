from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .polly_flush_stream_configuration import PollyFlushStreamConfiguration


class PollyTextEvent(BaseModel):
    Text: StrictStr
    TextType: Literal['ssml', 'text'] | None = None
    FlushStreamConfiguration: PollyFlushStreamConfiguration | None = None
