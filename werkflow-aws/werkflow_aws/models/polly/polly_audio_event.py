from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class PollyAudioEvent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    AudioChunk: StrictBytes | Any | None = None
